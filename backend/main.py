"""Main entry point"""
import env
from db import my_db, run_tests
from app import my_app, print_routes, send_verification_email
from flask_cors import CORS
from os import getenv
FLASK_PORT = getenv("FLASK_PORT")
if __name__ == '__main__' :
    #my_db.reset()
    #run_tests()
    #send_verification_email('skoukou007@gmail.com', "test")
    CORS(my_app, supports_credentials= True, origins="http://localhost:8080")
    my_app.run(port=FLASK_PORT)
    #print_routes(my_app)
    #result = my_db.execute_query("SELECT id, username FROM users", data_manip=False)
    #print(result)
    


