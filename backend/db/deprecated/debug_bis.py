import db.database as db
import os
class Debug():
    """Debug class containing functions to run some tests during production"""
    def __init__(self, db_path = db.DATABASE_LOCATION):
        self.db_path = db_path
        self.data = db.Database(db_path) 
    def drop_all_tables(self):
        """Remove all the tables from the database"""
        data = self.data
        database_path = data.db_path
        data.connect()
        conn = data.conn
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_sequence';")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        conn.commit()
        cursor.close()
        conn.close()
    def initiate_database(self):
        """Initiates the database using the database schema"""
        data = self.data
        with open(db.DATABASE_INIT_SQL_LOCATION) as sqlfile:
            script = sqlfile.read()
        data.execute_sql(script)
    def reset_database(self):
        """Clear everything in the database and recreate it using the creation script"""
        self.drop_all_tables()
        self.initiate_database()
    def run_tests(self, test_to_run = ""):
        """Define a function inside this function of the test you want to perform"""
        print(os.getenv("DB_PATH"))

