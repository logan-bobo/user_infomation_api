#!/usr/bin/env python3

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy, inspect
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@127.0.0.1:5001'
db = SQLAlchemy(app)

inspector = inspect(db.engine)

if not inspector.has_table('users'):
    # Schema Class
    class Users(db.Model):
        email = db.Column(db.String(100), nullable=False, primary_key=True)
        fname = db.Column(db.String(50), nullable=False)
        lname = db.Column(db.String(50), nullable=False)
        date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Create Schema
    db.create_all()




@app.route("/", methods=["GET"])
def root() -> str:
    return "User Information API please see the readme.md for details on how to interact with this service!"

# Create a user
@app.route("/create/{}", methods=["POST"])
def create () :
    return jsonify({"user": "create"})

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
