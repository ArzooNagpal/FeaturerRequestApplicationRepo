#importing SQLAlchemy class
from flask_sqlalchemy import SQLAlchemy
# importing flask object 'app'
from App import app

#Config class is used for configuring database and tablename 
class Config:
    # A string that tells SQLAlchemy where the database is and what the username and password are for that database.
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:Password0$@localhost:3306/FeatureRequestApp'
    #creating an object of SQLAlchemy class with parameter as application object
    db = SQLAlchemy(app)
    # declaring table name for model class
    tableName='FeatureRequestForm'
    