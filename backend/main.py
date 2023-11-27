"""Main entry point"""
import env
from db import my_db, run_tests
from app import my_app  
from os import *

API_VERSION = getenv("API_VERSION")      
if __name__ == '__main__' :
    #my_db.reset()
    #my_db.execute_sql()
    #run_tests()
    my_app.run()
    #result = my_db.execute_query("SELECT id, username FROM users", data_manip=False)
    #print(result)
    


