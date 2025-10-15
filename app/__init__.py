from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.user_routes import user_bp

    app.register_blueprint(user_bp, url_prefix='/user')

    @app.route('/')
    def index():
        return f'<h1>Pagina Principal da Fabrica de App'
    
    from .models import models

    return app