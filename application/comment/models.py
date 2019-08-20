from application import db
from sqlalchemy.sql import text
from datetime import datetime



class Comment (db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(), nullable=False)
    date_modified = db.Column(db.DateTime, nullable=True, onupdate = datetime.now())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    commentator = db.Column(db.String(20), nullable=False)

    text = db.Column(db.String(250), nullable=False)
    
    def __init__(self, commentator, text, date_created):
        self.commentator = commentator
        self.text = text
        self.date_created = date_created
    
    @staticmethod
    def find_comments_by_customer_id (id):
        stmt = text("SELECT id, text, commentator, date_created FROM comment"
                    " WHERE (customer_id = :id) ORDER BY date_created DESC").params(id=id)
        res = db.engine.execute(stmt)

        response  = []

        for row in res:
            response.append(row)
        
        return response

    @staticmethod
    def delete_comments_by_customer_id (id):
        stmt = text("DELETE FROM comment"
                    " WHERE (customer_id = :id)").params(id=id)
        db.engine.execute(stmt)


        
