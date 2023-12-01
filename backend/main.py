"""Main entry point"""
import env
from db import my_db, run_tests
from app import my_app, print_routes, send_verification_email
if __name__ == '__main__' :
    #my_db.reset()
    #run_tests()
    #send_verification_email('skoukou007@gmail.com', "test")
    my_app.run(port=5001)
    #print_routes(my_app)
    #result = my_db.execute_query("SELECT id, username FROM users", data_manip=False)
    #print(result)
    


