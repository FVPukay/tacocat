from flask import Flask, g, render_template
from flask_login import LoginManager, current_user

import models

DEBUG = True
HOST = 'localhost'
PORT = 8000

app = Flask(__name__)
app.secret_key = 'vlfTkFDU9UpQsyvxD0C8Pg'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


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
    tacos = models.Taco.select().limit(100)
    return render_template('index.html', tacos=tacos)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
