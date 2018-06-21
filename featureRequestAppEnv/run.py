#run.py is set to FLASK_APP to run flask environment
# from App package importing flask variable app
from App import app
#importing Config Class
from App.config import Config 

#Creating table with required columns
Config.db.create_all()

