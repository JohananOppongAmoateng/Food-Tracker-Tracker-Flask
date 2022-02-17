from flask import Blueprint
from . import db
# from flask_login import login_required,current_user


auth = Blueprint("auth",__name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    pass


@auth.route('/login',methods=['GET','POST'])
def login():
    pass

@auth.route('/logout')
def method_name():
    pass
