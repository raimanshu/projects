from flask import Blueprint, request, jsonify
from db.database import db
from models.order import Order

orders_bp = Blueprint('orders_bp', __name__)