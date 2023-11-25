"""Main entry point"""
import env
from db import my_db, run_tests, my_db_test
from app import api_blueprint, my_app
#from app import create_app     
from os import *
import unittest

API_VERSION = getenv("API_VERSION")      
if __name__ == '__main__' :
    # Create the db if it does not exist
    print(my_db_test.show_all_tables())
    #run_tests()
    


