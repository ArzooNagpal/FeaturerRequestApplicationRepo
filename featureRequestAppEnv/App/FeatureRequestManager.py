# featurerequestmanager.py acts as restful webservice which consists of 2 url used to create and retrieve Feature requests into/from database.
# Importing request, jsonify from flask package
from flask import request, jsonify
# Importing FeatureRequestForm model class
from App.featureRequestModel import FeatureRequestForm
# importing flask object 'app'
from App import app
# Imports FeatureAppServices class from featureAppServices.py
from App.featureRequestServices import FeatureAppServices

# FeatureRequestManger class is used to handle the url endpoints 'http://127.0.0.1:5000/createfeature' which is used to create Feature Requests and 'http://127.0.0.1:5000/retrievefeature' which is used to retrieve Feature Request records from database
class FeatureRequestManger:
    try:
        # createFeatureRequestManager function is used to create New Feature Request in Database
        @app.route("/createfeature",methods=['POST'])
        def createFeatureRequestManager():
            # Instance of FeatureAppServices class is created to access the function createFeatureService
            featureRequestServiceObject= FeatureAppServices()
            #Checking whether request method is POST
            if request.method == 'POST':
                # Assigning FeatureRequestForm class object with title, description,client,client priority,targetdate, productarea json values as arguments to createFeatureRequest function
                output= featureRequestServiceObject.createFeatureService(FeatureRequestForm(request.json['title'],request.json['description'],request.json['client'],request.json['clientPriority'],request.json['targetDate'],request.json['productArea']))
                return output
    #Surrounded with try except to handle any exception
    except Exception as e:
        print("Error occured in createFeatureRequestManager",e)

    try:
        # retrieveFeatureRequestManager function is used to retieve Feature Request from Database
        @app.route('/retrievefeature',methods = ['GET'])
        def retrievefeatureRequestManager():
            # Instance of FeatureAppServices class is created to access function retrieveFeatureService
            retrieveServiceObject =FeatureAppServices()
            #output from service fucntion retreiveFeatureService() is stored into retrievedDetails
            retrievedDetails=retrieveServiceObject.retreiveFeatureService()
            return jsonify({'ListFeature': retrievedDetails})
    #Surrounded with try except to handle any exception
    except Exception as e:
        print("Error Occured in retrieveFeatureRequestManager",e)