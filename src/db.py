import sqlite3 as sql


DATABASE_LOCATION = "res/data.db"

class Database:
    def __init__(self, db_path = DATABASE_LOCATION):
        self.db_path = db_path
    
    def connect(self):
        self.database = sql.connect(self.db_path)

    def execute_sql(self, query):
        return self.database.cursor().executescript(query)
    

    def create_deck(self, id, name):
        self.database.cursor().execute("""insert into decks (id, name) values (?, ?)""", (id, name))
        self.database.commit()