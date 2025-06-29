from app import create_app,db
from app.models import Register

from flask import jsonify, redirect, render_template,Blueprint,request, url_for
api_bp = Blueprint('api',__name__)

@api_bp.route('/')
def welcome():
    return render_template("Welcome.html")

@api_bp.route('/register')
def Registeration():
    return render_template("register.html")
@api_bp.route('/login')
def Login():
    return render_template("Login.html")

@api_bp.route("/ToDoList/<int:ID>")
def ToDoCreate(ID):
    return render_template("CreateToDoList.html",ID=ID)


@api_bp.route('/reg', methods=["POST", "GET"])
def register_user():
    
    if request.method == "POST":
        name = request.form['name']
        Email = request.form["email"]
        Password = request.form["password"]
        EnterPassword = request.form["Enterpassword"]
        if Password == EnterPassword:
            NewUser = Register(Name=name, Email=Email, Password=EnterPassword)
            db.session.add(NewUser)
            db.session.commit()
            return jsonify({"message": "Data Added Successfully"})
        else:
            return jsonify({"message": "Password and Re-Password is Different"})
@api_bp.route('/log', methods=["POST", "GET"])
def login_user():
    if request.method == "POST":
        Email = request.form["email"]
        Password = request.form["password"]
        data = Register.query.all()
        AllEmails = ([item.to_dict()["Email"] for item in data ])
        Registered = False 
        for i in AllEmails:
            if i == Email:
                Registered = True
                break
        if Registered == True:
            print(Registered)
            return redirect(url_for("api.ToDoCreate",ID=1))
        else:   
            return "Please Register"
@api_bp.route('/CreateToDoList/<int:ID>', methods=["POST", "GET"])
def CreateToDoList(ID):
    if request.method == "POST":
        Title = request.form["title"]
        Discription = request.form["discription"]
        Date = request.form["date"]
        Priority = request.form["Priority"]
        Status = False
        print(Title,Discription,Date,Priority,Status,ID)
        return "Hello"


        
