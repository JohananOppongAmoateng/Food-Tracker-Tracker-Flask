
from flask import  Blueprint
from . import db
# from flask_login import login_required,current_user

views = Blueprint("views",__name__)

@views.route('/',methods=["POST",'GET'])
def home():
    return "hello"