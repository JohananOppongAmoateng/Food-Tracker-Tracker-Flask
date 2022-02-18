
from flask import  Blueprint,render_template
from . import db
# from flask_login import login_required,current_user

views = Blueprint("views",__name__)

@views.route('/',methods=["POST",'GET'])
def home():
    return render_template('home.html')



@views.route('/foods',methods=['GET'])
def foods():
    return render_template('foods.html')