from flask import Flask
from routes import health
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from config.config import DevelopmentConfig, ProductionConfig
from flask_migrate import Migrate
import os



load_dotenv()

app = Flask(__name__)
database = SQLAlchemy()
migrate = Migrate(app, database)


if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)


database.init_app(app)
app.register_blueprint(health)