"""Main entry point"""
import env
from db import Debug
#from app import create_app     
from os import *
print(getcwd())

API_VERSION = getenv("API_VERSION")      
if __name__ == '__main__' :
    # Create the db if it does not exist
    debug = Debug()             #Debug contains db.Database object as the data field and will be used for testing purposes
    #app = create_app("config/development.py",API_VERSION)