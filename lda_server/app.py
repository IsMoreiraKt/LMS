from flask import Flask
from routes import health



app = Flask(__name__)
app.register_blueprint(health)