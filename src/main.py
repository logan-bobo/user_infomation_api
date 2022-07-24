import json

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../app.db"
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
def root() -> json:
    return jsonify(
        status="User Information API please see the readme.md for details on how to interact with this service!"
    ), 200


@app.route("/create-user", methods=["POST"])
def create() -> json:
    request_data = request.get_json()

    if "email" not in request_data:
        return jsonify(status="error", message="request did not contain the user email"), 400
    if "fname" not in request_data:
        return jsonify(status="error", message="request did not contain the users first name"), 400
    if "lname" not in request_data:
        return jsonify(status="error", message="request did not contain the users last name"), 400

    new_user = User(
        fname=request_data["fname"],
        lname=request_data["lname"],
        email=request_data["email"],
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(status="success", message="user created successfully"), 200
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify(status="error", message=f"unable to create user due to: {error}"), 500


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
    return jsonify(users_info), 200


@app.route("/read", methods=["GET"])
def read_user() -> json:
    request_data = request.get_json()

    user = User.query.filter_by(email=request_data["email"]).first()

    if user is None:
        return jsonify(status="error", message="user not found"), 400

    user_info = {
        "id": user.id,
        "fname": user.fname,
        "lname": user.lname,
        "email": user.email,
    }

    return jsonify(user_info), 200


@app.route("/update", methods=["PUT"])
def update() -> json:
    request_data = request.get_json()

    if "id" not in request_data:
        return jsonify(status="error", message="please supply a user ID"), 400

    if not any(key in request_data for key in ['fname', 'email', 'lname']):
        return jsonify(status="error", message="invalid parameters"), 400

    user = User.query.filter_by(id=request_data["id"]).first()

    if user is None:
        return jsonify(status="error", message="user not found"), 400

    if "fname" in request_data:
        user.fname = request_data['fname']
    if "email" in request_data:
        user.email = request_data['email']
    if "lname" in request_data:
        user.lname = request_data['lname']

    db.session.commit()

    return jsonify(status="success", message="User updated successfully"), 200


@app.route("/delete", methods=["DELETE"])
def delete() -> json:
    request_data = request.get_json()

    if "id" not in request_data:
        return jsonify(status="error", message="please supply a user ID"), 400

    user = User.query.get(request_data["id"])

    db.session.delete(user)
    db.session.commit()

    return jsonify(status="success", message="User removed successfully"), 200
