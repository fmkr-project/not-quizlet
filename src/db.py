import sqlite3 as sql


DATABASE_LOCATION = "res/data.db"

class Database:
    def __init__(self, db_path = DATABASE_LOCATION):
        self.db_path = db_path
    
    def connect(self):
        self.conn = sql.connect(self.db_path)

    def execute_sql(self, query):
        return self.conn.cursor().executescript(query)
    

    def create_deck(self, id, name):
        self.conn.cursor().execute("""insert into decks (id, name) values (?, ?)""", (id, name))
        self.conn.commit()
    
    def delete_deck(self, id):
        query = """DELETE FROM decks WHERE id = ?"""
        self.conn.cursor().execute(query, (id,))
        self.conn.commit()