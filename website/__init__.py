from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def blog():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = "bhaumik26"
    application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(application)

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix="/")
    application.register_blueprint(auth, url_prefix="/")

    from .models import User,Post

    create_database(application)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(application)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @application.route("/flask_crud")
    def flask_crud():
        return render_template("flask_crud.html")


    return application

def create_database(application):
    if not path.exists("website/"+DB_NAME):
        with application.app_context():
            db.create_all()
            print("Created DataBase !")