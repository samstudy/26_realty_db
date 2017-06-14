from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///media/sf_Projects/26_realty_dbassets.db'
app.secret_key = 'secret_key'
db = SQLAlchemy(app)