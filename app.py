from re import template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder='assets',template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/products_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONs'] = True
app.config["SECRET_KEY"] = "Products"
from controllers import *
from extensions import *
from models import *
if __name__ == '__main__':
    app.run(port=5000, debug=True)
