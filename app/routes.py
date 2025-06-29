from app import create_app,db
from app.models import Register

from flask import jsonify, render_template,Blueprint,request
api_bp = Blueprint('api',__name__)

@api_bp.route('/')
def Home():
    return render_template("register.html")

@api_bp.route('/register', methods=["POST", "GET"])
def register_user():
    if request.method == "POST":
        name = request.form['name']
        Email = request.form["email"]
        Password = request.form["password"]
        EnterPassword = request.form["Enterpassword"]
        if Password == EnterPassword:
            NewUser = Register(name=name, email=Email, password=EnterPassword)
            db.session.add(NewUser)
            db.session.commit()
            return jsonify({"message": "Data Added Successfully"})
        else:
            return jsonify({"message": "Password and Re-Password is Different"})

        
