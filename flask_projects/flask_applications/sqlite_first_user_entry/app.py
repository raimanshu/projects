from flask import Flask
from config import Config
from database import db
from api import api_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Hello, Flask with SQLAlchemy user management!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)