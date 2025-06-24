from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/profile", methods=["GET", "POST"])
def profile():
    user = {"username": "Miguel"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("profile.html", title="profile", user=user, posts=posts)


if __name__ == "__main__":
    # print(app.__dict__)
    app.run(debug=True, port=5001)
