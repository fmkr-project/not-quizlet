import sqlite3 as sql


DATABASE_LOCATION = "res/data.db"

class Database:
    def __init__(self, db_path = DATABASE_LOCATION):
        self.db_path = db_path
    
    def connect(self):
        """Connect to the database"""
        self.conn = sql.connect(self.db_path)

    def execute_sql(self, query):
        """Execute an SQL query"""
        return self.conn.cursor().executescript(query)
    

    def create_deck(self, id, name):
        """Create a new deck with an ID and a name"""
        self.conn.cursor().execute(f"insert into decks (id, name) values ({id}, '{name}')")
        self.conn.commit()
    
    def delete_deck(self, id):
        """Delete the deck with the given ID"""
        query = """DELETE FROM decks WHERE id = ?"""
        self.conn.cursor().execute(query, (id,))
        self.conn.commit()

    def switch_deck_favorite_state(self, id):
        """If the deck of given ID is favorited, unfavorite it, and vice-versa"""
        # Guard against non-existent decks
        favorite_flag = self.conn.cursor().execute("select favorite_tag from decks where id = ?", (id,)).fetchone()[0]
        if favorite_flag is None:
            print("This deck does not exist!")
            return
        favorite_flag = int(favorite_flag)
        
        self.conn.cursor().execute(f"update decks set favorite_tag = ? where id = ?", (1-favorite_flag, id,))

    def delete_card(self, id):
        """Delete the card with the given ID"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM cards WHERE id values (?)", (id,))
        self.conn.commit()
    def modify_card(self, id, new_front_side, new_back_side):
        """Modify the card with the given ID"""
        cursor = self.conn.cursor()
        query = "UPDATE cards SET front_side = ?, back_side = ? WHERE ID = ?"
        cursor.execute(query,(new_front_side, new_back_side, id))
        self.conn.commit()
    def modify_deck(self, id, name, description):
        """Modify the deck with the given ID"""
        cursor = self.conn.cursor()
        query = "UPDATE decks SET name = ?, description = ? WHERE id = ?"
        cursor.execute(query,(name, description, id))
        self.conn.commit()
