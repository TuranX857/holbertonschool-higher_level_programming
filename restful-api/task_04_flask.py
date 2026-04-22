#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# in-memory database
users = {}


# ROOT endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# /data -> bütün username-lər
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# /status
@app.route("/status")
def status():
    return "OK"


# /users/<username>
@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


# POST /add_user
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # user əlavə et
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


# run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
