import os

class Config:

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/chatbot")

  
    FLASK_ENV = os.getenv("FLASK_ENV", "development")  
    DEBUG = FLASK_ENV == "development" 
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  

  
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


config = Config()
