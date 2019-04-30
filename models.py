
################
#####MODELS#####
################

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Create our database model
class Person(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.Text)
    last = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Person {self.id}: {self.first} {self.last} {self.age}"
