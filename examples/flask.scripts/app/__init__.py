from flask import Flask

def create_app():
    app = Flask(__name__)

    #import blueprints
    from app.routers import auth, main

    #register blueprints
    app.register_blueprint(auth.auth,url_prefix='/auth')
    app.register_blueprint(main.main)

    return app