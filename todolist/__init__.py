import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]
# app.secret_key

db = SQLAlchemy()
migrate = Migrate(app, db)

db.init_app(app)
app.app_context().push()
