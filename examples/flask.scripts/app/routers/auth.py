from flask import blueprints

auth = blueprints.Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login Page'

@auth.route('/logout')
def logout():
    return 'Logout Page'