from flask import Flask, render_template, request, redirect, url_for
from config import Config


app = Flask(__name__)

# why config is added in tthe flask app ?
# why from_object is used when constant is stored in a class ?
app.config.from_object(Config) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Dummy check — replace with your real authentication logic
        if email == "test@gmail.com" and password == "password@123":
            return redirect(url_for('dashboard'))
        else:
            # Optionally, render login.html with an error message
            return render_template('login.html', error="Invalid email or password")

    return render_template('login.html')

# @app.route('/register', methods=['POST'])
# def register():
#     return render_template('register.html')

@app.route('/')
def index():
    return 'This is the default API when ever flask app starts running.'

@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"


if __name__ == '__main__':
    app.run(debug=True, port=5001)