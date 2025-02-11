from flask import Blueprint, render_template, request
from app.models.user import User
from app.extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'index'

@main.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email=email,password=password)
        #save user in database
        db.session.add(user)
        db.session.commit()
        return render_template('show.html')
    else:
        return render_template('create.html')

@main.route('/show')
def show():
    #users database showing new users first
    users = db.session.query(User).order_by(User.id.desc()).all()
    return render_template('show.html',users=users)