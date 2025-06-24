# api/__init__.py
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(err):
        return jsonify(error="Bad request", details=str(err)), 400

    @app.errorhandler(404)
    def not_found(err):
        return jsonify(error="Not found", details=str(err)), 404

    @app.errorhandler(500)
    def internal_error(err):
        return jsonify(error="Internal server error", details="Please try again later."), 500
