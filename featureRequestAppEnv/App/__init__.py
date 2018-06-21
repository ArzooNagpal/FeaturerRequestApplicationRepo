# Flask is a web application framework written in python.
#importing Flask class from flask package
from flask import Flask

# After importing Flask, we need to create an instance of the Flask class for our web application. Passing __name__ is going to configure flask.
app= Flask(__name__)
#importing views.py, FeatureRequestManager.py, featureAppServices.py, featureAppModel.py, config.py
from App import views,FeatureRequestManager,featureRequestModel,featureRequestServices,config 
