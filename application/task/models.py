from application import db

from sqlalchemy.sql import text


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    date = db.Column(db.DateTime)

    done = db.Column(db.Boolean, nullable=False)

    task_comment = db.Column(db.String(255), nullable=False)

    added_by_name = db.Column(db.String, nullable=False)

    completed_by_id = db.Column(db.Integer, nullable=True)

    customer_name = db.Column(db.String(255), nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customer.id'), nullable=False)
    # this is user.id
    added_by_id = db.Column(db.Integer,db.ForeignKey(
        'customer.id'), nullable=False)
    

    def __init__(self, date_created, date, done, task_comment, added_by_name, customer_name, customer_id, added_by_id):
        self.date_created = date_created
        self.date = date
        self.done = done
        self.task_comment = task_comment
        self.added_by_name = added_by_name
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.added_by_id = added_by_id
    
        

   
