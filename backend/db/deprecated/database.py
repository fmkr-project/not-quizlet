import sqlite3 as sql
from os import getenv
from werkzeug.security import check_password_hash
import mysql.connector
#### Determine if the database used is local or the one hosted
USE_LOCAL_DATABASE = (getenv("USE_LOCAL_DATABASE", "True") == True)

### Used if LOCAL_DATABASE = True
DATABASE_LOCATION = getenv("DB_PATH")
DATABASE_INIT_SQL_LOCATION = getenv("DB_SCHEMA")


### Used if LOCAL_DATABASE = False
AWS_DATABASE_ENDPOINT = getenv('AWS_DATABASE_ENDPOINT')
AWS_DATABASE_PORT = int(getenv('AWS_DATABASE_PORT', 3306))
AWS_DATABASE_USERNAME = getenv('AWS_DATABASE_USERNAME')
AWS_DATABASE_PASSWORD = getenv('AWS_DATABASE_PASSWORD')
AWS_DATABASE_NAME = getenv('AWS_DATABASE_NAME')

### JSON WEB-TOKENS
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")

class Database:
    def __init__(self, is_local = USE_LOCAL_DATABASE, db_path = DATABASE_LOCATION):
        """Creates an instance of the database class to make operations on the database"""
        self.db_path = db_path
        self.is_local = is_local
        self.conn = None
    def __repr__(self):
        """Representation of an instance of the Database class"""
        is_connected = self.conn is not None
        return f'''<Database object: 
        - Path = {self.db_path}
        - Connection = {is_connected}
        - Local = {self.is_local}>'''
    
    def connect(self):
        """Connect to the database"""
        if self.is_local:
            self.conn = sql.connect(self.db_path)
        else:
            db_config = {
                'user': AWS_DATABASE_USERNAME,
                'password': AWS_DATABASE_PASSWORD,
                'host': AWS_DATABASE_ENDPOINT,
                'port': AWS_DATABASE_PORT,
                'database': AWS_DATABASE_NAME
            }
    def close(self):
        """Disconnect the database"""
        if self.conn:
            self.conn.close()
        else:
            print("The Database is already closed")

    def execute_sql(self, script):
        """"Executes a SQL script (useful for making the setup of a schema)"""
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

    def user_exists_already(self, username=None, email=None):
        query = "SELECT 1 FROM users WHERE "
        params = ()

        if email and username:
            query += "email = ? OR username = ?"
            params = (email, username)
        elif email:
            query += "email = ?"
            params = (email,)
        elif username:
            query += "username = ?"
            params = (username,)
        else:
            return False

        self.connect()
        cur = self.conn.cursor()
        cur.execute(query, params)
        exists = cur.fetchone() is not None
        self.close()
        return exists
    def register_user(self, username, email, server_hash, salt):
        query, params = 'INSERT INTO users(username, email, password_hash, salt) VALUES(?,?,?,?)', (username, email, server_hash, salt)
        try:
            self.connect()
            cur = self.conn.cursor()
            cur.execute(query, params)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            self.close()
    def login_user(self, email, client_hashed_password):
        query, params = "SELECT password_hash, salt FROM users WHERE email = ?", (email)
        try:
            self.connect()
            cur = self.conn.cursor()
            cur.execute(query, params)
            user = cur.fetchone()
            if user and check_password_hash(user['password_hash'], client_hashed_password + user['salt']):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            self.close()


    def get_user_details(self, user_id):
        """Gets the user details considering his user_id"""
        query, params = "SELECT id, username, email, created_at FROM users WHERE id = ?", (user_id)
        try:
            self.connect()
            cur = self.conn.cursor()
            cur.execute(query, params)
            user_details = cur.fetchone()
            return user_details
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            self.close()

    def get_user_id_from_identifier(self, identifier, search_by_email=True):
        """Returns the user_id (None if not found) from an identifier that is either the email (by default) or the username"""
        if search_by_email:
            query, params = "SELECT id FROM users WHERE email = ?", (identifier)
        else:
            query, params = "SELECT id FROM users WHERE username = ?", (identifier)
        try:
            self.connect()
            cur = self.conn.cursor()
            cur.execute(query, params)
            user = cur.fetchone()
            return user["id"] if user else None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            self.close()
