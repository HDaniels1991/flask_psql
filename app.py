import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,IntegerField)
from wtforms.validators import DataRequired
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/my_website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Add on migration capabilities in order to run terminal commands
Migrate(app,db)

################
#####MODELS#####
################

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

################
#####FORMS######
################

class AddForm(FlaskForm):
    first = StringField('First Name',validators=[DataRequired()])
    last = StringField('Last Name',validators=[DataRequired()])
    age = IntegerField('Age',validators=[DataRequired()])
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    id = IntegerField('Id Person to Remove:')
    submit = SubmitField('Remove Person')

################
#####VIEWS######
################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        first = form.first.data
        last = form.last.data
        age = form.age.data
        new_person = Person(first=first,last=last,age=age)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('list_people'))
    return render_template('add.html',form=form)

@app.route('/del',methods=['GET','POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        person = Person.query.get(id)
        if person:
            db.session.delete(person)
            db.session.commit()
        return redirect(url_for('list_people'))
    return render_template('del.html',form=form)

@app.route('/list', methods=['GET','POST'])
def list_people():
    people = Person.query.all()
    return render_template('list.html', people=people)

if __name__ == '__main__':
    app.run(debug=True)
