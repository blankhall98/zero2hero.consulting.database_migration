from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#initialize app instance -----
app = Flask(__name__)

#configure database ----
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

#User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

#routes ----

##index route
@app.route('/')
def index():
    return render_template('index.html')

##CRUD routes

#Create
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    
    return render_template('create.html')

#Read
@app.route('/read')
def read():
    users = User.query.all()
    return render_template('read.html', users=users)

#Update
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    user = User.query.get(id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']

        db.session.commit()

        return redirect(url_for('read'))

    return render_template('update.html', user=user)

#Delete
@app.route('/delete/<int:id>')
def delete(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('read'))



#run application ----
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)