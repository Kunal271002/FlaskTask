from app import db

class Register(db.Model):
    __tablename__ = 'register'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class UserTask(db.Model):
    TaskId = db.Column(db.Integer, primary_key = True,autoincrement = True)
    UserId = db.Column(db.Integer,nullable = False)
    Status = db.Column(db.Integer,nullable = False)
    Title = db.Column(db.String(100),nullable = False)
    Description = db.Column(db.String(100),nullable = False)
    Due_Date = db.Column(db.String(100),nullable = False)
    Priority = db.Column(db.String(100),nullable = False)