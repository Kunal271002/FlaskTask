from app import db

class Register(db.Model):
    __tablename__ = 'register'
    UserId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "User_id": self.UserId,
            "Name": self.Name,
            "Email": self.Email,
            "Password":self.Password
        }


class UserTask(db.Model):
    TaskId = db.Column(db.Integer, primary_key = True,autoincrement = True)
    UserId = db.Column(db.Integer,nullable = False)
    Status = db.Column(db.Integer,nullable = False)
    Title = db.Column(db.String(100),nullable = False)
    Description = db.Column(db.String(100),nullable = False)
    Due_Date = db.Column(db.String(100),nullable = False)
    Priority = db.Column(db.String(100),nullable = False)

    
    def to_dict(self):
        return {
            "TaskId": self.TaskId,
            "User_id": self.UserId,
            "Status": self.Status,
            "Title": self.Title,
            "Description":self.Description ,      
            "Due_Date":self.Due_Date,
            "Priority":self.Priority       
        }
