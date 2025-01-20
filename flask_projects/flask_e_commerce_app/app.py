from flask import Flask


app = Flask(__name__)


with app.app_context():
    app.register_blueprint(user.api.bp, url_prefix='/api/users')
    app.register_blueprint(product.api.bp, url_prefix='/api/products')
    app.register_blueprint(order.api.bp, url_prefix='/api/orders')
    app.register_blueprint(payment.api.bp, url_prefix='/api/payments')
    app.register_blueprint(cart.api.bp, url_prefix='/api/cart')
    app.register_blueprint(inventory.api.bp, url_prefix='/api/inventory')


if __name__ == "__main__":
    app.run(debug=True)
