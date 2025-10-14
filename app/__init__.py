from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.user_routes import user_bp

    app.register_blueprint(user_bp, url_prefix='/user')

    @app.route('/')
    def index():
        return f'<h1>Pagina Principal da Fabrica de App'
    
    return app