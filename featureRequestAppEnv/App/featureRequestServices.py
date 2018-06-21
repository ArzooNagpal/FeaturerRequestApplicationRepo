#improting FeatureRequestForm class
from App.featureRequestModel import FeatureRequestForm
#importing Config class 
from App.config import Config
#importing all sqlalchemy exceptions from sqlalchemy package
from sqlalchemy.exc import *


# This is a service layer which provides create, reprioritize, retrieve functions.
class FeatureAppServices:
     # __init__ is default constructor used to declare a class level session variable which can be set or get whenever required for a session
    def __init__(self):
        self.session= ''

    # setSession function is used to set session variable for example to set mock sessions
    def setSession(self, argSession):
        self.session= argSession

    # getSession function is used to get session which is used to create and retrieve values
    def getSession(self):
        if self.session == '': 
            self.session= Config.db.session
            return self.session            
        else:            
            return self.session 

# This creates feature request and reprioritize it according the client priority.
    def createFeatureService(self,featureRequestForm):
        try:
            # Saving the client priority into reprioritizeStart variable
            reprioritizeStart= int(featureRequestForm.client_priority)
            # Saving the client  into reprioritizeClient variable
            reprioritizeClient= featureRequestForm.client
            # Checking rows for a particular client
            totalRows=len(self.getSession().query(FeatureRequestForm).filter_by(client = reprioritizeClient).all())
            # Checking whether given client priority less than or equal to total rows
            if reprioritizeStart <= totalRows:
                # Running for loop according to client Priority
                self.reprioritizeFeatureRequest(reprioritizeStart,totalRows,reprioritizeClient)
                self.getSession().add(featureRequestForm)
                
            # if given priority is greater than total number of rows then reprioritize as total+1 in client priority
            else:
                self.getSession().add(FeatureRequestForm(featureRequestForm.title, featureRequestForm.description, featureRequestForm.client, totalRows+1,featureRequestForm.target_date,featureRequestForm.product_area))

            #Commits all changes in a session to database   
            self.getSession().commit()
            #Returns a string response
            return 'success'

        #Surrounded with try except which can handle IntegrityError
        except IntegrityError as ie:
            #Rolling back session
            self.getSession().rollback()
            print("Title name already exists.Please change name.",ie)
            return 'Title name already exists.Please change name.'
        #Surrounded with try except which can handle any exception
        except Exception as e:
            #Rolling back session
            self.getSession().rollback()
            print("Error Occured in createFeatureRequestService",e)
            return 'Error Occured'
        #finaylly closes the session
        finally:
            self.getSession().close_all()

    # reprioritizeFeatureRequest function is used to reprioritize the Request Details from Database
    def reprioritizeFeatureRequest(self,reprioritizeStart,totalRows,reprioritizeClient):
        try:

            for reprioritizeStart in range(reprioritizeStart, totalRows+1, 1):
                reprioritizeRow = self.getSession().query(FeatureRequestForm).filter_by(client_priority=reprioritizeStart, client = reprioritizeClient).first()
                reprioritizeRow.Client_priority = reprioritizeStart+1
        # Surrounded with try except to handle any exceptions
        except Exception as e:
            #Rolling back session
            self.getSession().rollback()
            print("Error Occured in retrieveFeatureRequestService",e)
            return 'Error Occured'

        # Finally it closes the session
        finally:
            self.getSession().close_all()
       
    # retrieveFeatureService funcition is used to retrieve all the details of FeatureRequests and assigns it to array output
    def retreiveFeatureService(self):
        try:
            # Query the database to retrieve all rows and save in varaiable ListFeatures
            ListFeatures= FeatureRequestForm.query.all()
            output = []
            # Iterating the ListFeatures so each and every record are seperated and assigned to ListFeature_data tuple and in last each and every data tuple to output array
            for ListFeature in ListFeatures:
                ListFeature_data ={}
                #ListFeature_data['FeatureId']=ListFeature.FeatureId
                ListFeature_data['title']=ListFeature.title
                ListFeature_data['description']=ListFeature.description
                ListFeature_data['client']=ListFeature.client
                ListFeature_data['client_priority']=ListFeature.client_priority
                ListFeature_data['target_date']=ListFeature.target_date
                ListFeature_data['product_area']=ListFeature.product_area
                output.append(ListFeature_data)
            return output
        #Surrounded with try except which can handle any exception    
        except Exception as e:
            #Rolling back session
            self.getSession().rollback()
            print("Error Occured in retrieveFeatureRequestService",e)
            return 'Error Occured'
        #Finally close the session
        finally:
           self.getSession().close_all()

        

