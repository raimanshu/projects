from flask import Blueprint, current_app, jsonify
from database import db
from models import User

api_bp = Blueprint('api', __name__)

@api_bp.route('/create-default-user', methods=['POST'])
def create_default_user():
    email = "default@example.com"
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "Default user already exists."}), 200

    user = User(name="Default User", email=email)
    user.set_password("password123")

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": f"Default user created: {email} / password123"}), 201
