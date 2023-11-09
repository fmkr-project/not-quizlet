import sqlite3 as sql


DATABASE_LOCATION = "res/data.db"

class Database:
    def __init__(self, db_path = DATABASE_LOCATION):
        self.db_path = db_path
    
    def connect(self):
        """Connect to the database"""
        self.conn = sql.connect(self.db_path)

    def execute_sql(self, script):
        self.conn.executescript(script)

    def execute_query(self, query, params, data_manip = True):
        """Execute an SQL query"""
        self.connect()
        if data_manip:
            self.conn.execute(query, params)
            self.conn.commit()
        else:
            return self.conn.execute(query, params)
    
    def create_card(self, front_side, back_side):
        """Create a new card"""
        query, params = "INSERT INTO cards(front_side, back_side) VALUES (?,?)", (front_side, back_side)
        self.execute_query(query, params)
        
    def create_deck(self, name, description):
        """Create a new deck with a name and a description"""
        query, params = "INSERT INTO decks (name, description) VALUES (?,?)", (name, description)
        self.execute_query(query, params)

    def delete_deck(self, id):
        """Delete the deck with the given ID"""
        query, params = "DELETE FROM decks WHERE id = ?", (id)
        self.execute_query(query, params)

    def switch_deck_favorite_state(self, user_id, deck_id):
        """If the deck of given ID is favorited, unfavorite it, and vice-versa"""
        # Guard against non-existent decks
        query, params = "SELECT favorite_tag FROM users_links WHERE user_id = ? AND deck_id = ?", (user_id, deck_id)
        favorite_flag = self.execute_query(query, params, False).fetchone()[0]
        if favorite_flag is None:
            print("This deck does not exist!")
            return
        favorite_flag = int(favorite_flag)
        query_update, params_update = "UPDATE users_links SET favorite_tag = ? WHERE user_id = ? AND deck_id = ?", (1-favorite_flag, user_id, deck_id)
        self.execute_query(query_update, params)

    def delete_card(self, id):
        """Delete the card with the given ID"""
        query, params = "DELETE FROM cards WHERE id =?", (id)
        self.execute_query(query, params)

    def modify_card(self, id, new_front_side, new_back_side):
        """Modify the card with the given ID"""
        query, params = "UPDATE cards SET front_side = ?, back_side = ? WHERE ID = ?", (new_front_side, new_back_side, id)
        self.execute_query(query, params)

    def modify_deck(self, id, name, description):
        """Modify the deck with the given ID"""
        query, params = "UPDATE decks SET name = ?, description = ? WHERE id = ?", (name, description, id)
        self.execute_query(query, params)
