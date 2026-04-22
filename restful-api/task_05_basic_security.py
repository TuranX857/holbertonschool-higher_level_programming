#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT config
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# USERS (RAM-də)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ---------------- BASIC AUTH ----------------

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------------- LOGIN (JWT) ----------------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
        "username": username,
        "role": users[username]["role"]
    })

    return jsonify({"access_token": token})


# ---------------- JWT PROTECTED ----------------

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ---------------- ADMIN ONLY ----------------

@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
