from db.database import db


# Define the many-to-many association table
order_items = db.Table(
    'order_items',
    db.Column('order_id', db.String(36), db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.String(36), db.ForeignKey('products.id'), primary_key=True)
)

# # Patch models with the actual table
# Product.orders.property.secondary = order_items
# Order.products.property.secondary = order_items


# Import models
# from .user import User
# from .product import Product
# from .order import Order


