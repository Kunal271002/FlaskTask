from app import db

class Register(db.Model):
    UserId = db.Column(db.Integer, primary_key = True,autoincrement = True)
    Name = db.Column(db.String(100),nullable = False)
    Email = db.Column(db.String(100),nullable = False)
    Password = db.Column(db.String(100),nullable = False)

class UserTask(db.Model):
    TaskId = db.Column(db.Integer, primary_key = True,autoincrement = True)
    UserId = db.Column(db.Integer,nullable = False)
    Status = db.Column(db.Integer,nullable = False)
    Title = db.Column(db.String(100),nullable = False)
    Description = db.Column(db.String(100),nullable = False)
    Due_Date = db.Column(db.String(100),nullable = False)
    Priority = db.Column(db.String(100),nullable = False)