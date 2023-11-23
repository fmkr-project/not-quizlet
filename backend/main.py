"""Main entry point"""
import env
from db import Debug, my_db
from app import api_blueprint, my_app
#from app import create_app     
from os import *

API_VERSION = getenv("API_VERSION")      
if __name__ == '__main__' :
    # Create the db if it does not exist
    debug = Debug()
    debug.reset_database()


