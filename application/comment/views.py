from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.customers.models import Customer
from application.comment.models import Comment
from application.auth.models import User
from application.customers.forms import CustomerForm
from application.comment.forms import CommentForm
from application.task.forms import TaskForm



@app.route("/comments/<customer_id>/delete/<comment_id>", methods=["POST"])
@login_required
def comment_delete(comment_id, customer_id):

    comment = Comment.query.get(comment_id)
    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("customer_page", id=customer_id))


@app.route("/comments/<customer_id>/edit/<comment_id>", methods=["GET", "POST"])
@login_required
def comment_edit(comment_id, customer_id):

    comment = Comment.query.get(comment_id)
    customer = Customer.query.get(customer_id)
    form = CommentForm()

    if request.method == "GET":

        form.text.data = comment.text
        
        return render_template("comments/comment.html", comment=comment, form=form, customer=customer)

    elif request.method == "POST":
        
        comment.text = request.form.get("text")

        db.session().commit()

        return redirect(url_for("customer_page", id=customer.id))

    


