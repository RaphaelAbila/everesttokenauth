from flask import Flask,Blueprint
from flask_cors import CORS
from flask_mysqldb import MySQL
from settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB,MYSQL_USER1, MYSQL_PASSWORD1, MYSQL_DB1
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@127.0.0.1/user_authentication'
app.config['SQLALCHEMY_BINDS']={
    'grader': "mysql://root:@127.0.0.1/everestg_grader",
    'campus': "mysql://root:@127.0.0.1/everestg_campus_kayiwa"
}
app.debug =0

db = SQLAlchemy(app)

from blueprint_auth import authentication

app.register_blueprint(authentication, url_prefix="/api/auth")
