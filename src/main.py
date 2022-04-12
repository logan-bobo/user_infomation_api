#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy, inspect

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:mysecretpassword@127.0.0.1:5001"
db = SQLAlchemy(app)

inspector = inspect(db.engine)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


if not inspector.has_table("users"):
    # Create Schema
    db.create_all()

# Root
@app.route("/", methods=["GET"])
def root() -> str:
    return "User Information API please see the readme.md for details on how to interact with this service!"


# Create a user
@app.route("/create", methods=["POST"])
def create():
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


# Return all users
@app.route("/read", methods=["GET"])
def read():
    return jsonify({"user": "read"})


# Read the data of a specific user
@app.route("/read/{id}", methods=["GET"])
def read_all():
    return jsonify({"user": "read"})


# Update a user
@app.route("/update/{id}", methods=["PUT"])
def update():
    return jsonify({"user": "update"})


# Delete a user
@app.route("/delete/{id}", methods=["DELETE"])
def delete():
    return jsonify({"user": "delete"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
