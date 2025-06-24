# app.py
from flask import Flask
from config import Config
from db.database import db
from api.users import users_bp
from api.products import products_bp
from api.orders import orders_bp
from db.seed import load_initial_data
from api import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_error_handlers(app)


    with app.app_context():
        db.create_all()
        load_initial_data()

    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(orders_bp, url_prefix='/api/orders')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)
