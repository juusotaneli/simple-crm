from application import app, db
import timestring

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.customers.models import Customer
from application.comment.models import Comment
from application.auth.models import User
from application.comment.forms import CommentForm
from application.task.models import Task
from application.task.forms import TaskForm
from datetime import datetime, timedelta, date




@app.route("/tasks/today", methods=["GET"])
@login_required
def show_scheduled_tasks():

    tasks = Task.query.filter(Task.date <= datetime.now()).filter(Task.done == False).order_by(Task.date.asc())

    return render_template("task/tasks.html", date=datetime.now(), tasks=tasks, show_today = True, number_of_tasks = tasks.count(), can_be_assigned = True)


# @app.route("/customers/addtask/<id>", methods=["GET"])
# @login_required
# def get_tasks(id):
#    form = TaskForm(request.form)
    # if form.validate_on_submit():
#    return form.date.data.strftime('%Y-%m-%d')
    # return render_template("task/task.html", form=form)

# shows tasks for one week ahead
@app.route("/tasks/week", methods=["GET"])
@login_required
def show_scheduled_tasks_week():

    tasks=Task.query.filter(Task.date < (datetime.now() + timedelta(days=7)), Task.date > datetime.now()).filter(Task.done == False).order_by(Task.date.asc())
    
    return render_template("task/tasks.html", date=datetime.now(), tasks=tasks, number_of_tasks = tasks.count(), show_week = True, can_be_assigned = True)


@app.route("/tasks/tomorrow", methods=["GET"])
@login_required
def show_scheduled_tasks_tomorrow():

    tasks=Task.query.filter(Task.date < (datetime.now() + timedelta(days=1)), Task.date > datetime.now()).filter(Task.done == False).order_by(Task.date.asc())
    
    return render_template("task/tasks.html", date=datetime.now(), tasks=tasks, number_of_tasks = tasks.count(), show_tomorrow = True,  can_be_assigned = True)

@app.route("/tasks/month", methods=["GET"])
@login_required
def show_scheduled_tasks_month():

    tasks = Task.query.filter(Task.date < (datetime.now() + timedelta(days=30)), Task.date > datetime.now()).filter(Task.done == False).order_by(Task.date.asc())
    
    return render_template("task/tasks.html", date=datetime.now(), tasks=tasks, number_of_tasks = tasks.count(), show_month = True, can_be_assigned = False)

# shows all finished tasks
@app.route("/tasks/history", methods=["GET"])
@login_required
def show_history():

    tasks = Task.query.filter(Task.done == True).order_by(Task.date.desc())

    return render_template("task/tasks.html", date=datetime.now(), tasks=tasks, show_history = True, number_of_tasks = tasks.count())

@app.route("/customers/addtask/<id>", methods=["POST"])
@login_required
def add_task(id):

    if (timestring.Date(request.form.get("date")) < datetime.date(datetime.now())):
        return redirect(url_for("customer_page_with_error", id=id))
    
    t = Task(datetime.now(), timestring.Date(request.form.get("date")).date, False, request.form.get(
        "task_comment"), current_user.firstname + " " + current_user.surename, Customer.query.get(id).name, id, current_user.id)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("customer_page", id=id))


@app.route("/task/<id>", methods=["GET"])
@login_required
def show_task(id):
    return render_template("task/task.html", task=Task.query.get(id))

@app.route("/task/<id>", methods=["POST"])
@login_required
def finish_task(id):
    t = Task.query.get(id)
    t.done = True
    t.completed_by_id = current_user.id

    db.session().commit()

    return redirect(url_for("show_scheduled_tasks"))
