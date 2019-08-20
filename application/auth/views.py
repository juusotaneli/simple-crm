from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, f_bcrypt, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm, PasswordForm


import pygal

from datetime import datetime



@login_required(role="ANY")
@app.route("/")
def index():
    if (current_user.is_authenticated):
        return redirect(url_for("show_scheduled_tasks"))

    return redirect(url_for("auth_login"))


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data.lower()).first()


    # tarkastetaan onko käyttäjä olemassa ja kontrolloidaan kirjautumiskertoja.
    # jos kirjautumisyrityksiä on yli kolme kirjautuminen estetään

    if user:
        if f_bcrypt.check_password_hash(user.password, form.password.data) is False and user.failed_logins < 3:
            user.failed_logins += 1
            db.session().commit()
            return render_template("auth/loginform.html", form=form, error=True, error_msg="Käyttäjätunnus tai salasana väärin")

        elif user.failed_logins == 3:
            return render_template("auth/loginform.html", form=form, error=True, error_msg="Tili lukittu. Ota yhteys ylläpitoon.")

        elif user.is_active() is False:
            return render_template("auth/loginform.html", form=form, error=True, error_msg="Tilisi ei ole aktiivinen. Ota yhteys ylläpitoon.")

        elif f_bcrypt.check_password_hash(user.password, form.password.data) and user.failed_logins < 3:
            login_user(user)
            user.failed_logins = 0
            user.last_login = datetime.now()
            db.session().commit()
            return redirect(url_for("show_scheduled_tasks"))

    return render_template("auth/loginform.html", form=form, error=True, error_msg="Käyttäjätunnus tai salasana väärin")


@app.route("/auth/logout")
@login_required(role="ANY")
def auth_logout():
    logout_user()
    return render_template("auth/loginform.html", form=LoginForm())


@app.route("/auth/new", methods=["GET", "POST"])
@login_required(role="admin")
def auth_create():
    if request.method == "GET":
        return render_template("auth/new.html", form=UserForm())

    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form=form)

    elif form.password.data != form.re_password.data:
        return render_template("auth/new.html", form=UserForm(), passwords_dont_match=True)

    elif User.query.filter_by(username=request.form.get("username").lower()).scalar() is None:

        u = User(form.firstname.data, form.surename.data, form.username.data.lower(
        ), f_bcrypt.generate_password_hash(form.password.data).decode('utf8'), form.role.data, True, 0)

        db.session().add(u)
        db.session().commit()
        

        return redirect(url_for("show_scheduled_tasks"))

    return render_template("auth/new.html", form=UserForm(), username_taken=True)


@app.route("/auth/new-password", methods=["GET", "POST"])
@login_required(role="ANY")
def update_password():

    form = PasswordForm(request.form)

    if request.method == "GET":
        return render_template("auth/update_password.html", form=form)

    if not form.validate():
        return render_template("auth/update_password.html", form=form)

    elif (form.new_password.data == form.new_password_again.data):
        current_user.password = f_bcrypt.generate_password_hash(form.new_password.data).decode('utf8')
        db.session().commit()
        return redirect(url_for("show_scheduled_tasks"))

    return render_template("auth/update_password.html", form=form, passwords_dont_match=True)


@app.route("/auth/control", methods=["GET", "POST"])
@login_required(role="admin")
def auth_control():
    users = User.query.order_by(User.firstname.desc()).all() 

    if request.method == "GET":
        return render_template("auth/auth_control.html", users=users, datetime=datetime, current_user = current_user)

@app.route("/auth/control/reset_password/<id>", methods=["GET", "POST"])
@login_required(role="admin")
def reset_password(id):
    form = PasswordForm(request.form)
    u = User.query.get(id)


    if request.method == "GET":
        return render_template("auth/reset_password.html", form=form, current_user = current_user, user = u)

    if not form.validate():
        return render_template("auth/reset_password.html", form=form, user = u)

    elif (form.new_password.data == form.new_password_again.data):
        u.failed_logins = 0
        u.password = f_bcrypt.generate_password_hash(form.new_password.data).decode('utf8')
        db.session().commit()
        return redirect(url_for("auth_control"))

    return render_template("auth/reset_password.html", form=form, passwords_dont_match=True, user = u)
    
    

@app.route("/auth/deactivate/<id>", methods=["GET", "POST"])
@login_required(role="admin")
def auth_deactivate(id):
    users = User.query.order_by(User.firstname.desc()).all() 

    if request.method == "POST":
        u = User.query.get(id)
        u.active_status = False
        db.session().commit()

        return render_template("auth/auth_control.html", users=users, datetime=datetime, current_user = current_user)

@app.route("/auth/activate/<id>", methods=["POST"])
@login_required(role="admin")
def auth_activate(id):
    users = User.query.order_by(User.firstname.desc()).all() 
    
    if request.method == "POST":
        u = User.query.get(id)
        u.active_status = True
        db.session().commit()
    
    return render_template("auth/auth_control.html", users=users, datetime=datetime, current_user = current_user)

@app.route("/statistics")
@login_required(role="ANY")
def user_statistics():
    bar_chart_comments = pygal.Bar()
    for u in User.number_of_comments_posted_by_user():
        bar_chart_comments.add(u.commentator, u.count)

    chart_comments = bar_chart_comments.render(is_unicode=True)

    bar_chart_tasks = pygal.Bar()
    for u in User.number_of_tasks_initiated_by_user():
        bar_chart_tasks.add(u.firstname + " " + u.surename, u.count)

    chart_tasks = bar_chart_tasks.render(is_unicode=True)

    return render_template("auth/statistics.html", user_comments=User.number_of_comments_posted_by_user(), user_tasks=User.number_of_tasks_initiated_by_user(), chart=chart_comments, chart1=chart_tasks)
