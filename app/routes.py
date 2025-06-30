from app import create_app,db
from app.models import Register,UserTask

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

@api_bp.route('/CreateToDoList/<int:ID>', methods=["POST", "GET"])
def AddTask(ID):
    return render_template("CreateToDoList.html",ID=ID)

@api_bp.route("/ToDoList/<int:ID>")
def ToDoCreate(ID):
    data = UserTask.query.all()
    All = [item.to_dict() for item in data ]
    Value = list(filter(lambda x: (x["User_id"] == ID), All))
    print(Value)
    return render_template("ToDoTask.html",ID=ID,value=Value)

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
        All = [item.to_dict() for item in data ]
        Value = list(filter(lambda x: (x["Email"] == Email and x["Password"] == Password), All))
        try:
            Id = Value[0]["User_id"]
        except:
            return "Your Password is wrong or You are not Registered"
        Registered =  bool(Value)
        if Registered == True:
            print(Registered)
            return redirect(url_for("api.ToDoCreate",ID=Id))
        else:   
            return "Your Password is wrong or You are not Registered"

@api_bp.route('/AddTask/<int:ID>', methods=["POST", "GET"])
def CreateToDoList(ID):
    if request.method == "POST":
        Title = request.form["title"]
        Discription = request.form["discription"]
        Date = request.form["date"]
        Priority = request.form["Priority"]
        Status = False
        try:
            NewUser = UserTask(UserId=ID, Status=Status, Title=Title,Description=Discription,Due_Date=Date,Priority=Priority)
        except:
            return jsonify({"message": "Data Not Added Successfully"})
        else:
            db.session.add(NewUser)
            db.session.commit()
            return jsonify({"message": "Data Added Successfully"})

        
