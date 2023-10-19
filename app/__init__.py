"""
    The `create_app` function is used to create and configure a Flask application, including setting up
    CORS, database, and registering blueprints for different routes.
    :return: The function `create_app()` returns the Flask application object `app` after registering
    the blueprints and initializing the database.
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate

# The line `from alx_capstone_projectapp.routes.auth import auth_bp` is importing the `auth_bp`
# blueprint from the `routes.auth` module in the `alx_capstone_projectapp` package. This blueprint is
# likely used to define and handle authentication routes in the Flask application.

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # CORS(app)
    # CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://example.com"]}})

    try:
        app.config.from_object(Config)
        db.init_app(app)
        migrate = Migrate(app, db)
        # print(db)
        from app.routes.main import main
        from app.routes.auth import auth_bp
        from app.routes.user import user_bp

        app.register_blueprint(main)
        app.register_blueprint(auth_bp)
        app.register_blueprint(user_bp)
        try:
            # print(app.app_context())
            with app.app_context():
                db.create_all()
                # session = db.session
                return app
        except Exception as e:
            print(e)
        
    except Exception as e:
        print(e,"failed config")
