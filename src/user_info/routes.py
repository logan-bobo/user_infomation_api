import json

from . import app, db
from .models import User
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError


@app.route("/v1/", methods=["GET"])
def root() -> json:
    return jsonify(
        status="User Information API V1 please see the readme.md for details on how to interact with this service!"
    ), 200


@app.route("/v1/users", methods=["POST"])
def create_user() -> json:
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
        error = str(e)
        return jsonify(status="error", message=f"unable to create user due to: {error}"), 500


@app.route("/v1/users", methods=["GET"])
def read_users() -> json:
    users_info = []

    users = User.query.order_by(User.uid).all()

    for user in users:
        users_info.append({
            "uid": user.uid,
            "fname": user.fname,
            "lname": user.lname,
            "email": user.email,
        })
    return jsonify(users_info), 200


@app.route("/v1/users/<int:uid>", methods=["GET"])
def read_user(uid: int) -> json:
    user = User.query.filter_by(uid=request.view_args["uid"]).first()

    if user is None:
        return jsonify(status="error", message="user not found"), 400

    user_info = {
        "id": user.uid,
        "fname": user.fname,
        "lname": user.lname,
        "email": user.email,
    }

    return jsonify(user_info), 200


@app.route("/v1/users/<int:uid>", methods=["PUT"])
def update_user(uid: int) -> json:
    request_data = request.get_json()

    if not any(key in request_data for key in ['fname', 'email', 'lname']):
        return jsonify(status="error", message="invalid parameters"), 400

    user = User.query.filter_by(uid=request.view_args["uid"]).first()

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


@app.route("/v1/users/<int:uid>", methods=["DELETE"])
def delete_user(uid: int) -> json:
    user = User.query.get(request.view_args["uid"])

    db.session.delete(user)
    db.session.commit()

    return jsonify(status="success", message="User removed successfully"), 200
