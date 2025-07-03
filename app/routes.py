from app import create_app,db
import bcrypt
from app.models import Register,UserTask
from flask_jwt_extended import create_access_token,jwt_required

from flask import jsonify, redirect, render_template,Blueprint,request, url_for
api_bp = Blueprint('api',__name__)

@api_bp.route('/')
def welcome():
    return render_template("Welcome.html")

@api_bp.route('/register')
def Registeration():
    return render_template("register.html")

@api_bp.route('/login')
# @jwt_required
def Login():
    return render_template("Login.html")

@api_bp.route('/UpdateToDoList/<int:ID>', methods=["POST", "GET"])
# @jwt_required

def UpdateToDoList(ID):
    return render_template("Update_Page.html",ID=ID)

@api_bp.route('/CreateToDoList/<int:ID>', methods=["POST", "GET"])
# @jwt_required

def AddTask(ID):
    return render_template("CreateToDoList.html",ID=ID)

@api_bp.route("/ToDoList/<int:ID>")
# @jwt_required
def ToDoCreate(ID):
    data = UserTask.query.all()
    All = [item.to_dict() for item in data ]
    Value = list(filter(lambda x: (x["User_id"] == ID), All))
    return render_template("ToDoTask.html",ID=ID,value=Value)

@api_bp.route('/reg', methods=["POST", "GET"])
def register_user():
    if request.method == "POST":
        name = request.form['name']
        Email = request.form["email"]
        Password = request.form["password"]
        EnterPassword = request.form["Enterpassword"]
        if Password == EnterPassword:
            bytes = EnterPassword.encode('utf-8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)
            NewUser = Register(Name=name, Email=Email, Password=hash)
            db.session.add(NewUser)
            db.session.commit()
            return jsonify({"message": "Data Added Successfully"})
        else:
            return jsonify({"message": "Password and Re-Password is Different"})
        
@api_bp.route('/log', methods=["POST", "GET"])
# @jwt_required
def login_user():
    if request.method == "POST":
        Email = request.form["email"]
        Password = request.form["password"]
        userBytes = Password.encode('utf-8')
        data = Register.query.all()
        All = [item.to_dict() for item in data]
        Value = list(filter(lambda x: x["Email"] == Email, All))
        if not Value:
            return "You are not registered."
        access_token = create_access_token(identity=Email)
        user = Value[0]["Password"]
        stored_hashed_password = user
        if bcrypt.checkpw(userBytes, stored_hashed_password.encode('utf-8')):
            print(user)
            Id = Value[0]["User_id"]
            return redirect(url_for("api.ToDoCreate", ID=Id))
        else:
            return "Your password is wrong."

@api_bp.route('/AddTask/<int:ID>', methods=["POST", "GET"])
# @jwt_required
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
        
@api_bp.route('/CompletedToDoList/<int:ID>', methods=["POST", "GET"])
# @jwt_required

def CompletedToDoList(ID):
    Data = UserTask.query.get_or_404(ID)
    Data.Status = 1
    db.session.commit()
    return "Status Has been Udated"

@api_bp.route('/Update/<int:ID>', methods=["POST", "GET"])
# @jwt_required

def Update(ID):
    if request.method == "POST":
        Title = request.form["title"]
        discription = request.form["discription"]
        Date = request.form["date"]
        Priority = request.form["Priority"]
        try:
            Status = request.form["Completed"]
            Status = 1
        except:
            Status = 0
    else:
        data = request.get_json()
        Title = data["title"]
        discription = data["discription"]
        Date = data["date"]
        Priority = data["Priority"]
        Status = data["Completed"]
    Data = UserTask.query.get_or_404(ID)
    Data.Status = Status
    Data.Title = Title
    Data.Description = discription
    Data.Due_Date = Date
    Data.Priority = Priority
    db.session.commit()
    print(Title,discription,Date,Priority,Status)
    return "Status Has been Udated"

@api_bp.route('/DeleteToDoList/<int:ID>', methods=["POST", "GET"])
# @jwt_required
def DeleteToDoList(ID):

    Data = UserTask.query.get_or_404(ID)
    db.session.delete(Data)
    db.session.commit()
    return "Task Has been Deleted"

    

        
