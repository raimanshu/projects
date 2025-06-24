# models/mixins.py
from datetime import datetime
from db.database import db

class AuditMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(36), nullable=True)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(36), nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    deleted_by = db.Column(db.String(36), nullable=True)
