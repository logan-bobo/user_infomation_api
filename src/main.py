#!/usr/bin/env python3

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy, inspect
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@127.0.0.1:5001'
db = SQLAlchemy(app)

inspector = inspect(db.engine)

# Schema Class
class Users(db.Model):
    email = db.Column(db.String(100), nullable=False, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

if not inspector.has_table('users'):
    # Create Schema
    db.create_all()

@app.route("/", methods=["GET"])
def root() -> str:
    return "User Information API please see the readme.md for details on how to interact with this service!"

# Create a user
@app.route("/create", methods=["POST"])
def create():
    request_data = request.get_json()
    print(request_data)

    request_email = None
    request_fname = None
    request_lname = None

    if 'email' in request_data:
        request_email = request_data["email"]
    else:
        return "Request did not contain the user email", 400
    
    if 'fname' in request_data:
        request_fname = request_data["fname"]
    else:
        return "Request did not contain the users first name", 400
    
    if 'lname' in request_data:
        request_lname = request_data["lname"]
    else:
        return "Request did not contain the users last name", 400

    db.engine.execute(Users.insert().values(email=request_email, fname=request_fname, lname=request_lname))
    
    return "User data created sucsesfully", 200

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
