from flask import render_template, flash, redirect, url_for, blueprints
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from app.forms.users import LoginForm
from app.models.users import User
from app.models.spiders import Spider
from app.forms.spiders import SpiderForm
from app.extensions import db

users = blueprints.Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@users.route('/add_spider', methods=['GET', 'POST'])
@login_required
def add_spider():
    form = SpiderForm()
    if form.validate_on_submit():
        spider = Spider(
            scientific_name=form.scientific_name.data,
            characteristic_1=form.characteristic_1.data,
            characteristic_2=form.characteristic_2.data,
            characteristic_3=form.characteristic_3.data,
        )
        db.session.add(spider)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_spider.html', form=form)
