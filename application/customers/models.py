from application import db
from sqlalchemy.sql import text


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate=db.func.current_timestamp()

    name = db.Column(db.String(255), nullable=False)
    erp_id = db.Column(db.String(20), nullable=False)

    route = db.Column(db.String(5), nullable=True)

    contact_person = db.Column(db.String(255), nullable=True)

    phone_number = db.Column(db.String(255), nullable=True)

    email = db.Column(db.String(255), nullable=True)

    comments = db.relationship("Comment", backref='account', lazy=True)

    def __init__(self, name, erp_id, route, contact_person, phone_number, email):
        self.name = name
        self.erp_id = erp_id
        self.route = route
        self.contact_person = contact_person
        self.phone_number = phone_number
        self.email = email
        
    @staticmethod
    def delete_tasks_by_customer_id (id):
        stmt = text("DELETE FROM task"
                    " WHERE (customer_id = :id)").params(id=id)
        db.engine.execute(stmt)
    
    @staticmethod
    def find_all_customers_matching_given_string (string):
        stmt = text("SELECT * FROM customer"
                    " WHERE name LIKE :string").params(string=string)
                    
        db.engine.execute(stmt)

        res = db.engine.execute(stmt)

        response  = []

        for row in res:
            response.append(row)
        
        return response


    
    
    

    


