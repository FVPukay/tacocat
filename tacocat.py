from flask import Flask, g

import models

DEBUG = True
HOST = 'localhost'
PORT = 8000

app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
def index():
    return "This is the index URL"


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
