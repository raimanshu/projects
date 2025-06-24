import uuid
# from db.database import db
from .mixins import AuditMixin
from models import db, order_items

# order_items = None  # Will be initialized in models/__init__.py


class Product(db.Model, AuditMixin):
    __tablename__ = 'products'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    orders = db.relationship('Order', secondary=order_items, back_populates='products')
    created_by = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)


