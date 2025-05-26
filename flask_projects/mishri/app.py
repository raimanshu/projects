from flask import Flask
from config import Config


app = Flask(__name__)

# why config is added in tthe flask app ?
# why from_object is used when constant is stored in a class ?
app.config.from_object(Config) 

@app.route('/')
def index():
    return 'This is the default API when ever flask app starts running.'


if __name__ == '__main__':
    app.run(debug=True, port=5001)