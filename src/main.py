#!/usr/bin/env python3

import os
from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, Text, MetaData, Table, inspect

engine = create_engine('postgresql://postgres:mysecretpassword@127.0.0.1:5001')

metadata = MetaData()

if not inspect(engine).has_table("user_info"):
    user_info = Table(
        'user_info', metadata,
        Column('user_email', Text, primary_key=True),
        Column('fname', Text),
        Column('lname', Text),
        Column('mobile_number', Integer),
    )
    user_info.create(bind=engine)

insert_user = user_info.insert().values(user_email='test@user.com', fname='test', lname='user', mobile_number= 1234567898 )
engine.execute(insert_user)

app = Flask(__name__)

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
