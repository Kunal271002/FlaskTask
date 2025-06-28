from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:redhat@localhost/flipkartdb" 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    app.config["JWT_SECRET_KEY"] = 'super-secret-key' 

    jwt.init_app(app)
    db.init_app(app)

    from app.routes import api_bp
    # from app.auth import auth_bp
    app.register_blueprint(api_bp)
    # app.register_blueprint(auth_bp)


    return app

