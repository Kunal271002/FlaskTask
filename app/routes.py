from app import create_app
from flask import render_template,Blueprint,request
api_bp = Blueprint('api',__name__)

@api_bp.route('/')
def Home():
    return render_template("register.html")

@api_bp.route('/register',methods=["POST","GET"])
def Register():
    # if request.method=="POST":
    name = request.form['name']
    Email = request.form["email"]
    Password = request.form["password"]
    print(name,Email,Password)
    return f"{name}"
