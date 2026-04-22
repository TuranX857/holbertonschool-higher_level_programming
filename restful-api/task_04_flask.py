#!/usr/bin/python3
"""Simple Flask API with users management."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """API status endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_data():
    """Return list of usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Get a specific user."""
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
