#!/usr/bin/env python3

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy, inspect

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = os.environ['DATABASE_URL']
# "postgresql://postgres:mysecretpassword@127.0.0.1:5001"
db = SQLAlchemy(app)

inspector = inspect(db.engine)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

if not inspector.has_table("users"):
    db.create_all()

@app.route("/", methods=["GET"])
def root() -> str:
    return "User Information API please see the readme.md for details on how to interact with this service!"

@app.route("/create-user", methods=["POST"])
def create() -> str:
    request_data = request.get_json()

    if "email" not in request_data:
        return "Request did not contain the user email", 400
    if "fname" not in request_data:
        return "Request did not contain the users first name", 400
    if "lname" not in request_data:
        return "Request did not contain the users last name", 400

    new_user = User(
        fname=request_data["fname"],
        lname=request_data["lname"],
        email=request_data["email"],
    )

    db.session.add(new_user)
    db.session.commit()
    return "User created sucsesfully\n", 200

@app.route("/read-users", methods=["GET"])
def read_users():
    users_info = {}
    users = User.query.order_by(User.fname).all()
    for user in users:
        users_info[user.id] = {
            "fname": user.fname,
            "lname": user.lname, 
            "email": user.email,
        }
    return jsonify(users_info)


@app.route("/read/<int:user_id>", methods=["GET"])
def read_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    user_info = {
        "fname": user.fname,
        "lname": user.lname,
        "email": user.email,
    }
    return jsonify(user_info)


@app.route("/update/<int:user_id>", methods=["PUT"])
def update():
    return jsonify({"user": "update"})


@app.route("/delete/<int:user_id>", methods=["DELETE"])
def delete():
    return jsonify({"user": "delete"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
