from flask import Flask
from backend.config import Config
from backend.database import db
from backend.middleware import init_middleware
from backend.api_routes import register_routes

app = Flask(__name__)
Config.init_app(app)
db.init_app(app)
init_middleware(app)
register_routes(app)

if __name__ == "__main__":
    app.run()