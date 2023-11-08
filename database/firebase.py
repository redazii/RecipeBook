import firebase_admin
import pyrebase
from config.firebase_config import firebaseConfig


#from dotenv import dotenv_values
#import json
#env = dotenv_values(dotenv_path='.env')

if not firebase_admin._apps :
    cred = firebase_admin.credentials.Certificate("c:/Users/redaz/Downloads/myapi-8a340-firebase-adminsdk-3uwum-0face33b2c.json")
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#authentication
authRecipe = firebase.auth()