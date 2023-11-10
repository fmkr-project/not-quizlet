import sqlite3 as sql
import env
from os import getenv
DATABASE_LOCATION = getenv("DB_PATH")
DATABASE_INIT_SQL_LOCATION = getenv("DB_SCHEMA")

class Database:
    def __init__(self, db_path = DATABASE_LOCATION):
        self.db_path = db_path
        self.conn = None
    def connect(self):
        """Connect to the database"""
        self.conn = sql.connect(self.db_path)
    def execute_sql(self, script):
        self.connect()
        self.conn.executescript(script)
        self.conn.close()
    def execute_query(self, query, params, data_manip=True):
        """Execute an SQL query"""
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            if data_manip:
                self.conn.commit()
            else:
                # Fetch all rows if the query is meant to retrieve data
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        finally:
            cursor.close()
            self.conn.close()
    
    def create_card(self, front_side, back_side):
        """Create a new card"""
        query, params = "INSERT INTO cards(front_side, back_side) VALUES (?,?)", (front_side, back_side)
        self.execute_query(query, params)
    def modify_card(self, id, new_front_side, new_back_side):
        """Modify the card with the given ID"""
        query, params = "UPDATE cards SET front_side = ?, back_side = ? WHERE ID = ?", (new_front_side, new_back_side, id)
        self.execute_query(query, params)
    def delete_card(self, id):
        """Delete the card with the given ID"""
        query, params = "DELETE FROM cards WHERE id =?", (id)
        self.execute_query(query, params)
        
    def create_deck(self, name, description):
        """Create a new deck with a name and a description"""
        query, params = "INSERT INTO decks (name, description) VALUES (?,?)", (name, description)
        self.execute_query(query, params)
    def modify_deck(self, id, name, description):
        """Modify the deck with the given ID"""
        query, params = "UPDATE decks SET name = ?, description = ? WHERE id = ?", (name, description, id)
        self.execute_query(query, params)
    def delete_deck(self, id):
        """Delete the deck with the given ID"""
        query, params = "DELETE FROM decks WHERE id = ?", (id)
        self.execute_query(query, params)

    def switch_deck_favorite_state(self, user_id, deck_id):
        """If the deck of given ID is favorited, unfavorite it, and vice-versa"""
        query, params = "SELECT favorite_tag FROM users_links WHERE user_id = ? AND deck_id = ?", (user_id, deck_id)
        result = self.execute_query(query, params, False)
        # If there is no such row, then the deck does not exist for the user
        if not result:
            print("This deck does not exist!")
            return False
        favorite_flag = int(result[0][0])
        new_favorite_flag = 1 if favorite_flag == 0 else 0 
        query_update, params_update = "UPDATE users_links SET favorite_tag = ? WHERE user_id = ? AND deck_id = ?", (new_favorite_flag, user_id, deck_id)
        self.execute_query(query_update, params_update, True)
        return True
    def get_decks_user(self, user_id):
        query, params = "SELECT deck_id FROM users_links WHERE user_id = ?", (user_id)
        result = self.execute_query(query, params, False)
        return result
    def get_cards_of_deck(self, deck_id):
        query, params = "SELECT card_id FROM card_links WHERE deck_id = ?", (deck_id)
        result = self.execute_query(query, params, False)
        return result





