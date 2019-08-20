from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.customers.models import Customer
from application.comment.models import Comment
from application.auth.models import User
from application.task.models import Task
from application.customers.forms import CustomerForm
from application.comment.forms import CommentForm
from application.task.forms import TaskForm


from datetime import datetime



@app.route("/customers/new/")
@login_required(role=("ANY"))
def customers_form():
    return render_template("customers/new.html", form=CustomerForm())


@app.route("/customers/", methods=["POST"])
@login_required(role=("ANY"))
def customers_create():
    form = CustomerForm(request.form)

    if not form.validate():
        return render_template("customers/new.html", form=form)
    # tarkistaa että lisättyä asiakasta ei ole vielä tarkistamalla tietokannasta
    # löytyykö asiakas syötetyllä nimellä tai erp_idellä --purkkaratkaisu--
    # todo: validaattorit formiin.
    elif Customer.query.filter_by(name=request.form.get("name").upper()).scalar() is not None:
        return render_template("customers/new.html", error1=True, form=form)
    elif Customer.query.filter_by(erp_id=request.form.get("erp_id")).scalar() is not None:
        return render_template("customers/new.html", error2=True, form=form)

    c = Customer(form.name.data.upper(), form.erp_id.data, form.route.data,
                 form.contact_person.data, form.phone_number.data, form.email.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("customer_page", id=c.id))


@app.route("/search", methods=["POST", "GET"])
@login_required(role=("ANY"))
def customers_search():
    search = request.form.get("search").upper()
    customers = Customer.query.all()

    for customer in customers:
        if customer.name == search or customer.erp_id == search:
            return redirect(url_for("customer_page", id=customer.id))

    search_by_name = Customer.query.filter(Customer.name.contains(
        search)).order_by('name').limit(10)

    search_by_erp_id = Customer.query.filter(Customer.erp_id.contains(
        search)).order_by('name').limit(10)

    if search_by_name.count() is 0 and search_by_erp_id.count() is 0:
        return render_template("customers/customer_search_results.html", no_hits=True)
    elif search_by_name.count() is not 0:
        return render_template("customers/customer_search_results.html", customers=search_by_name)
    elif search_by_erp_id.count() is not 0:
        return render_template("customers/customer_search_results.html", customers=search_by_erp_id)

@app.route("/customers/<id>", methods=["POST", "GET"])
@login_required(role=("ANY"))
def customer_page(id):
    customer = Customer.query.get(id)

    if request.method == "GET":
        comments = Comment.find_comments_by_customer_id(id)
        tasks = Task.query.filter(Task.done != True).filter(
            Task.customer_id == id).order_by(Task.date)
        if len(comments) == 0:
            return render_template("customers/customer.html", customer=customer, date = datetime.now(),
                                   no_comments=True, tasks=tasks,
                                   form=CommentForm(), taskform=TaskForm(),
                                   datetime=datetime, logged_in_user=current_user)

        return render_template("customers/customer.html", customer=customer, date = datetime.now(),
                               comments=comments, tasks=tasks,
                               form=CommentForm(), taskform=TaskForm(),
                               datetime=datetime, logged_in_user=current_user)
    # lisätään kommentti 'seinälle'. todo: tämä pitää siirää oikeen luokkaan eli comment -viewsien alle
    elif request.method == "POST":
        c = Comment(current_user.firstname + " " + current_user.surename, request.form.get(
            "text"), datetime.now())

        c.customer_id = id

        c.account_id = current_user.id

        db.session().add(c)
        db.session().commit()

        return redirect(url_for("customer_page", id=customer.id))


@app.route("/customers/<id>/taskerror", methods=["POST", "GET"])
@login_required(role=("ANY"))
def customer_page_with_error(id):
    customer = Customer.query.get(id)
    comments = Comment.find_comments_by_customer_id(id)
    tasks = Task.query.filter(Task.done != True).filter(
        Task.customer_id == id).order_by(Task.date)

    return render_template("customers/customer.html", customer=customer,
                           comments=comments, tasks=tasks,
                           form=CommentForm(), taskform=TaskForm(),
                           datetime=datetime, logged_in_user=current_user, error=True)


@app.route("/customers/delete/<id>", methods=["POST"])
@login_required(role=("admin"))
def customer_delete(id):

    Comment.delete_comments_by_customer_id(id)

    Customer.delete_tasks_by_customer_id(id)

    customer = Customer.query.get(id)
    db.session().delete(customer)
    db.session().commit()

    return redirect(url_for("index"))


@app.route("/customers/update/<id>", methods=["GET", "POST"])
@login_required(role=("ANY"))
def customer_update(id):
    customer = Customer.query.get(id)
    form = CustomerForm(request.form)

    # jos käyttäjä antaa uuden nimen ja / tai erp_id:m, tarkastetaan ettei nimeä/idtä ole jo käytössä jollain muulla asiakkaalla.
    # jos molemmat arvot ovat muuttumattomat, tallennetaan suoraan tietokantaan.
    if request.method == "POST":
        if request.form.get("name").upper() != customer.name and Customer.query.filter_by(name=request.form.get("name").upper()).scalar() is not None:
            return render_template("customers/updatepage.html", error1=True, form=form, customer=customer)

        elif request.form.get("erp_id") != customer.erp_id and Customer.query.filter_by(erp_id=request.form.get("erp_id")).scalar() is not None:
            return render_template("customers/updatepage.html", error2=True, form=form, customer=customer)

        else:
            customer.name = request.form.get("name").upper()
            customer.erp_id = request.form.get("erp_id")
            customer.route = request.form.get("route")
            customer.contact_person = request.form.get("contact_person")
            customer.phone_number = request.form.get("phone_number")
            customer.email = request.form.get("email")

            db.session().commit()

            return redirect(url_for("customer_page", id=customer.id))

    else:
        form = CustomerForm(request.form)
        return render_template("customers/updatepage.html", form=form, customer=customer)

# --- tätä ominaisuutta ei tarvita ---- #

#@app.route("/customers/update/<id>/add-responsible-person", methods=["POST"])
#@login_required
#def customer_add_person_responsible(id):
#    customer = Customer.query.get(id)
#    customer.persons_in_response.append(current_user)
#    db.session.commit()
#    return redirect(url_for("customer_page", id=customer.id))
