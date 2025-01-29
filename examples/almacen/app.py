from extensions import app, db
from flask import render_template, request, url_for, redirect, session

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///almacen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

#Modelos
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False,unique=True)
    price = db.Column(db.Float,nullable=False)
    stock = db.Column(db.Integer,nullable=False,default=True)

#Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    session['user'] = 'admin'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('index'))

@app.route('/add_item',methods=['GET','POST'])
def add_item():

    if 'user' not in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            name = request.form['name']
            price = request.form['price']
            stock = request.form['stock']

            item = Item(name=name,price=price,stock=stock)
            db.session.add(item)
            db.session.commit()

            return redirect(url_for('items',method='all'))

        return render_template('add_item.html')
    

@app.route('/items/<method>')
def items(method):
    if 'user' not in session:
        return redirect(url_for('index'))
    else:
        if method == 'all':
            items = Item.query.all()
        elif method == 'price':
            items = Item.query.order_by(Item.price).all()
        elif method == 'stock':
            items = Item.query.order_by(Item.stock.desc()).all()
        return render_template('items.html',items=items)
    
@app.route('/delete_item/<int:id>')
def delete_item(id):
    if 'user' not in session:
        return redirect(url_for('index'))
    else:
        item = Item.query.get(id)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('items',method='all'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)