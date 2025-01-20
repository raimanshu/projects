class Config:

    SECRET_KEY = '123456789'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db' 