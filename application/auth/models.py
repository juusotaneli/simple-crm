from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    firstname = db.Column(db.String(144), nullable=False)
    surename = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    active_status = db.Column(db.Boolean, default=True, nullable=False)
    failed_logins = db.Column(db.Integer, nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

    def __init__(self, firstname, surename, username, password, role, active_status, failed_logins):
        self.firstname = firstname
        self.surename = surename
        self.username = username
        self.password = password
        self.role = role
        self.active_status = active_status
        self.failed_logins = failed_logins
  
    def get_id(self):
        return self.id

    def is_active(self):
        return self.active_status

    def is_authenticated(self):
        return True

    def get_role(self):
        return self.role

    @staticmethod
    def number_of_comments_posted_by_user():
        stmt = text("SELECT Comment.commentator, COUNT (*) as count FROM Comment"
                    " LEFT JOIN Account ON Comment.account_id = Account.id WHERE Account.active_status = True"
                    " GROUP BY Comment.commentator")
        
        res = db.engine.execute(stmt)

        response  = []

        for row in res:
            response.append(row)
        
        return response
    
    @staticmethod
    def number_of_tasks_initiated_by_user():
        stmt = text("SELECT Account.firstname, Account.surename, COUNT (*) as count FROM Account"
                    " INNER JOIN Task ON Task.added_by_id = Account.id WHERE Account.active_status = True"
                    " GROUP BY Account.firstname, Account.surename")
                
        res = db.engine.execute(stmt)

        response  = []

        for row in res:
            response.append(row)
        
        return response
