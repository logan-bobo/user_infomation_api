from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import inspect

app = Flask(__name__)
app.register_blueprint()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../app.db"

db = SQLAlchemy(app)

inspector = inspect(db.engine)

if not inspector.has_table("users"):
    db.create_all()

from . import routes
