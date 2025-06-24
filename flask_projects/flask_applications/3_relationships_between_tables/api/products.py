from flask import Blueprint, request, jsonify
from db.database import db
from models.product import Product

products_bp = Blueprint('products_bp', __name__)