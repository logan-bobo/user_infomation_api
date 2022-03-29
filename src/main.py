#!/usr/bin/env python3

from pymongo import MongoClient
from flask import Flask, jsonify

client = MongoClient("mongodb://test:test@localhost:5001/")
db = client.user_info 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "User Information API please see the readme.md for details on how to interact with this service!"

# Create a user
@app.route("/create/{}", methods=["POST"])
def create ():
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
