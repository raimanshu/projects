from flask import Blueprint, request, jsonify
from db.database import db
from models.user import User

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    u = User(name=data['name'], email=data['email'])
    u.set_password(data['password'])
    db.session.add(u)
    db.session.commit()
    return jsonify(id=u.id), 201

@users_bp.route('/', methods=['GET'])
def list_users():
    return jsonify([{"id":u.id,"name":u.name,"email":u.email} for u in User.query.all()])

@users_bp.route('/<uid>', methods=['GET'])
def get_user(uid):
    u = User.query.get_or_404(uid)
    return jsonify(name=u.name, email=u.email)

@users_bp.route('/<uid>', methods=['PUT'])
def update_user(uid):
    u = User.query.get_or_404(uid)
    data = request.json
    u.name = data.get('name', u.name)
    u.email = data.get('email', u.email)
    db.session.commit()
    return jsonify(success=True)

@users_bp.route('/<uid>', methods=['DELETE'])
def delete_user(uid):
    u = User.query.get_or_404(uid)
    db.session.delete(u)
    db.session.commit()
    return jsonify(success=True), 204
