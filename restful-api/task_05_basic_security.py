#!/usr/bin/python3
"""Flask API with Basic Auth + JWT + Role-based access."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Basic Auth
auth = HTTPBasicAuth()

# Users (username -> data)
users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    },
    "user1": {
        "password": generate_password_hash("user123"),
        "role": "user"
    }
}

# -------------------------
# BASIC AUTH
# -------------------------

@auth.verify_password
def verify(username, password):
    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth Access Granted"})


# -------------------------
# JWT LOGIN
# -------------------------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users[username]

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify({"token": token})


# -------------------------
# JWT PROTECTED ROUTE
# -------------------------

@app.route("/protected")
@jwt_required()
def protected():
    return jsonify({"message": "JWT Access Granted"})


# -------------------------
# ROLE BASED ACCESS
# -------------------------

@app.route("/admin")
@jwt_required()
def admin_only():
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admins only"}), 403

    return jsonify({"message": "Welcome Admin!"})


@app.route("/user")
@jwt_required()
def user_route():
    claims = get_jwt()

    if claims.get("role") not in ["user", "admin"]:
        return jsonify({"error": "Access denied"}), 403

    return jsonify({"message": "User access granted"})


# -------------------------
# RUN SERVER
# -------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
