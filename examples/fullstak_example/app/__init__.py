from .extensions import app, db, login_manager

def create_app():
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.models.users import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    #register blueprints
    from app.routers import users, main
    app.register_blueprint(users.users)
    app.register_blueprint(main.main)


    #create database
    from app.models import spiders, users
    with app.app_context():
        db.create_all()
    
    return app

