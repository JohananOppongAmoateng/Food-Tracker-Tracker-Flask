from flask import Blueprint,render_template
from . import db
# from flask_login import login_required,current_user


auth = Blueprint("auth",__name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def method_name():
    pass
