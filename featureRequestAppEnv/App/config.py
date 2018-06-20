from flask_sqlalchemy import SQLAlchemy 
from App import app

class Config:
    # A string that tells SQLAlchemy where the database is and what the username and password are for that database.
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:Password0$@localhost:3306/FeatureRequestApp'
    #creating an object of SQLAlchemy class with parameter as application object
    db = SQLAlchemy(app)
    