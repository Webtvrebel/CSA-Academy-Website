import os
from flask import Flask
from .config import Config
from .routes import init_routes
from .models import init_db   # 👈 ADD THIS

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    os.makedirs(app.instance_path, exist_ok=True)

    init_routes(app)

    # 👇 ADD THIS BLOCK
    with app.app_context():
        init_db()

    return app