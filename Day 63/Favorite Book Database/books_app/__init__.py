from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'mysecretcombinationisamysteryforyou'

    # Import models here to avoid circular import
    from .models import Book

    # Initialize the SQLAlchemy extension
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Import views after creating app and initializing the database
    from .views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
