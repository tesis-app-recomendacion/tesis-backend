from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import bp  # ✅ Importa el Blueprint
    app.register_blueprint(bp)

    return app
