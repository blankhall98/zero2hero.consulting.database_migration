from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app.extensions import db
from app.models import User, Item

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/queries',methods=['GET','POST'])
def queries():
    return render_template('queries.html')

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':

        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or user.password != request.form['password']:
            flash('Invalid username or password')
            return render_template('login.html')
        else:
            session['username'] = request.form['username']
            return redirect(url_for('main.queries'))
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('main.index'))