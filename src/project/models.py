from . import db
from sqlalchemy import inspect

inspector = inspect(db.engine)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


if not inspector.has_table("users"):
    db.create_all()
