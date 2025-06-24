import uuid
from models import db, order_items
from models.mixins import AuditMixin  # if AuditMixin is in a mixins.py


class Order(db.Model, AuditMixin):
    __tablename__ = "orders"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    created_by = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    total = db.Column(db.Float, nullable=False)

    # Explicit foreign_keys declaration to resolve ambiguity
    user = db.relationship(
        "User", foreign_keys=[user_id], backref=db.backref("orders", lazy=True)
    )

    # Optional: if you want to track who created the order (e.g. an admin)
    created_user = db.relationship(
        "User",
        foreign_keys=[created_by],
        backref=db.backref("created_orders", lazy=True),
    )

    products = db.relationship(
        "Product", secondary=order_items, back_populates="orders"
    )
