from flask import Flask

DEBUG = True
HOST = 'localhost'
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the index URL"


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
