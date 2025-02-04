from app.extensions import app, db

def create_app():

    #register blueprints
    from app.views import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    #create the database models
    from app.models import User, Item
    with app.app_context():
        db.create_all()

    return app