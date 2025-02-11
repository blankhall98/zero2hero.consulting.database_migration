from flask import Flask

def create_app():

    app = Flask(__name__)

    #registrar blueprint
    from app.views.main import main
    app.register_blueprint(main)

    #inicializar base de datos
    from app.extensions import db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app