from App import app
# Importing SQL Alchemy class from the flask_sqlalchemy module
#from sqlalchemy import Sequence
from App.config import Config 

# A class FeatureRequestForm will be the class to which we will map the table and contains required columns from table as variables in class.
class FeatureRequestForm(Config.db.Model):
    __tablename__='FeatureRequestForm'
   # FeatureId = Config.db.Column('FeatureId', Config.db.Integer(), Sequence('feature_id_seq'),unique=True,primary_key=True)
    title = Config.db.Column(Config.db.String(100), unique= True,primary_key=True)
    description = Config.db.Column(Config.db.String(2000))
    client = Config.db.Column(Config.db.String(50))  
    client_priority= Config.db.Column(Config.db.Integer())
    target_date = Config.db.Column(Config.db.Date())
    product_area = Config.db.Column(Config.db.String(50))
# __init__ is a constructor method for a class.It is called whenever an object of the class is constructed.
    def __init__(self, title, description, client,client_priority,target_date,product_area):
        self.title= title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area = product_area

#INSERT INTO `FeatureRequestForm` (`Title`, `Description`, `Client`, `Client_priority`, `Target_date`, `Product_area`) VALUES ('title 34', 'desc 34', 'Client B', 1, '2018-06-22', 'Policies')