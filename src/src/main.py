#!/usr/bin/env python3

import json
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"name": "test"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)