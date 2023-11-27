from os import getenv, path
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text

# Environment Variables
USE_LOCAL_DATABASE_ENV = getenv("USE_LOCAL_DATABASE", "True").lower() == "true"
DB_PATH = getenv("DB_PATH")
DB_TEST_PATH = getenv("DB_TEST_PATH")
DB_SCHEMA = getenv("DB_SCHEMA")
AWS_DATABASE_ENDPOINT = getenv('AWS_DATABASE_ENDPOINT')
AWS_DATABASE_PORT = getenv('AWS_DATABASE_PORT', '3306')
AWS_DATABASE_USERNAME = getenv('AWS_DATABASE_USERNAME')
AWS_DATABASE_PASSWORD = getenv('AWS_DATABASE_PASSWORD')
AWS_DATABASE_NAME = getenv('AWS_DATABASE_NAME')
AWS_DATABASE_TEST_NAME = getenv('AWS_DATABASE_TEST_NAME')
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")

class Database:
    def __init__(self, is_local = USE_LOCAL_DATABASE_ENV, is_test = False):
        """Creates an instance of the database class to make operations on the database"""
        self.is_test = is_test
        self.is_local = is_local
        if is_local:
            self.database_uri = f'sqlite:///{DB_TEST_PATH if is_test else DB_PATH}'
        else:
            self.database_uri = (
                f"mysql+mysqlconnector://{AWS_DATABASE_USERNAME}:{AWS_DATABASE_PASSWORD}@"
                f"{AWS_DATABASE_ENDPOINT}:{AWS_DATABASE_PORT}/"
                f"{AWS_DATABASE_TEST_NAME if is_test else AWS_DATABASE_NAME}")
        self.engine = create_engine(self.database_uri, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None
    def __repr__(self):
        """Representation of an instance of the Database class"""
        is_connected = self.session is not None
        if self.is_local:
            s = f"""<Database object:
        - Test Database = {self.is_test},
        - Connection = {is_connected},
        - Local = {self.is_local}
        - Database URI = {self.database_uri}>"""
        
        else:
            s = f"""<Database object:
        - Test Database = {self.is_test},
        - Connection = {is_connected},
        - Host = {AWS_DATABASE_ENDPOINT},
        - Port = {AWS_DATABASE_PORT},
        - User = {AWS_DATABASE_USERNAME},
        - Database = {AWS_DATABASE_NAME}
        - Database URI = {self.database_uri}>"""
        return s

    def connect(self):
        """Connect to the database"""
        self.session = self.Session()
    def close(self):
        """Disconnect the database"""
        if self.session:
            self.session.close()
            self.session = None
        else:
            return False

    def execute_query(self, query, params={}, data_manip=True):
        """Execute an SQL query"""
        try:
            self.connect()
            if data_manip:
                self.session.execute(text(query), params)
                self.session.commit()
            else:
                result_proxy = self.session.execute(text(query), params)
                result = [dict(row) for row in result_proxy.mappings()]
                return result
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            if data_manip:
                self.session.rollback()  # Rollback in case of data manipulation error
            raise
        finally:
            self.close()
    def execute_sql(self, script_path = DB_SCHEMA):
        """Executes a SQL script from a provided file path."""
        try:
            self.connect()
            with open(script_path, 'r') as file:
                sql_script = file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    self.session.execute(text(statement.strip()))
            self.session.commit()
        except SQLAlchemyError as e:
            print(f"An error occurred while executing SQL script: {e}")
            self.session.rollback()
            raise
        except IOError as e:
            print(f"Error opening file: {e}")
            raise
        finally:
            self.close()
    def drop_all_tables(self):
        """Drops all tables in the database."""
        try:
            self.connect()
            meta = MetaData()
            meta.reflect(bind=self.engine)
            meta.drop_all(bind=self.engine)
            print("All tables have been dropped successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        finally:
            self.close()
    def reset(self):
        self.drop_all_tables()
        self.execute_sql()
    def show_all_tables(self):
        """Shows all the tables of the database"""
        if self.is_local:
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
                tables = [row[0] for row in result]
            return tables
        else:
            query = "SHOW tables"
            return self.execute_query(query)



    def get_card_by_id(self, card_id):
        """Gets the card with that id"""
        query = "SELECT * FROM cards WHERE id = :card_id"
        params = {'card_id': card_id}
        return self.execute_query(query, params)
    def create_card(self, front_side, back_side, creator_id = 0):
        """Create a new card"""
        query = "INSERT INTO cards (front_side, back_side, creator_id) VALUES (:front_side, :back_side, :creator_id)"
        params = {'front_side': front_side, 'back_side': back_side, 'creator_id': creator_id}
        self.execute_query(query, params)
    def modify_card(self, card_id, new_front_side, new_back_side):
        """Modify the card with the given ID"""
        query = "UPDATE cards SET front_side = :new_front_side, back_side = :new_back_side WHERE id = :card_id"
        params = {'new_front_side': new_front_side, 'new_back_side': new_back_side, 'card_id': card_id}
        self.execute_query(query, params)
    def delete_card(self, card_id):
        """Delete the card with the given ID"""
        query = "DELETE FROM cards WHERE id = :card_id"
        params = {'card_id': card_id}
        self.execute_query(query, params)
    def delete_card_completely(self, card_id):
        """Delete a card completely from the database."""
        delete_links_query = "DELETE FROM card_links WHERE card_id = :card_id"
        self.execute_query(delete_links_query, {'card_id': card_id})
        delete_card_query = "DELETE FROM cards WHERE id = :card_id"
        self.execute_query(delete_card_query, {'card_id': card_id})
    def delete_card_from_deck(self, card_id, deck_id):
        """Remove a specific card from a deck."""
        delete_query = "DELETE FROM card_links WHERE card_id = :card_id AND deck_id = :deck_id"
        self.execute_query(delete_query, {'card_id': card_id, 'deck_id': deck_id}) 
    def add_card_to_deck(self, card_id, deck_id):
        """Adds a card to a deck"""
        query = "INSERT INTO card_links (card_id, deck_id) VALUES (:card_id, :deck_id)"
        self.execute_query(query, {'card_id': card_id, 'deck_id': deck_id}, True)



    def get_deck_by_id(self, deck_id):
        """Gets the deck with that id"""
        query = "SELECT * FROM decks WHERE id = :card_id"
        params = {'deck_id': deck_id}
        return self.execute_query(query, params)            
    def create_deck(self, name, description, creator_id=0):
        """Create a new deck with a name and a description."""
        query = "INSERT INTO decks (name, description, creator_id) VALUES (:name, :description, :creator_id)"
        params = {'name': name, 'description': description, 'creator_id': creator_id}
        self.execute_query(query, params)
    def modify_deck(self, deck_id, name, description):
        """Modify the deck with the given ID."""
        update_query = "UPDATE decks SET name = :name, description = :description WHERE id = :deck_id"
        params = {'name': name, 'description': description, 'deck_id': deck_id}
        self.execute_query(update_query, params)
    def delete_deck_from_user(self, deck_id, user_id):
        """Remove the deck from the user's list but keep it in the database."""
        delete_query = "DELETE FROM users_links WHERE deck_id = :deck_id AND user_id = :user_id"
        self.execute_query(delete_query, {'deck_id': deck_id, 'user_id': user_id})
    def delete_deck_completely(self, deck_id):
        """Delete the deck completely from the database."""
        delete_links_query = "DELETE FROM users_links WHERE deck_id = :deck_id"
        self.execute_query(delete_links_query, {'deck_id': deck_id})
        delete_deck_query = "DELETE FROM decks WHERE id = :deck_id"
        self.execute_query(delete_deck_query, {'deck_id': deck_id})
    def switch_deck_favorite_state(self, user_id, deck_id):
        """If the deck of given ID is favorited, unfavorite it, and vice-versa"""
        select_query = "SELECT favorite_tag FROM users_links WHERE user_id = :user_id AND deck_id = :deck_id"
        select_params = {'user_id': user_id, 'deck_id': deck_id}
        result = self.execute_query(select_query, select_params, False)
        if not result:
            print("This deck does not exist!")
            return False        
        favorite_flag = int(result[0][0])
        new_favorite_flag = 1 if favorite_flag == 0 else 0
        update_query = "UPDATE users_links SET favorite_tag = :new_favorite_flag WHERE user_id = :user_id AND deck_id = :deck_id"
        update_params = {'new_favorite_flag': new_favorite_flag, 'user_id': user_id, 'deck_id': deck_id}
        self.execute_query(update_query, update_params, True)
        return True


    def get_decks_user(self, user_id):
        query = "SELECT deck_id FROM users_links WHERE user_id = :user_id"
        params = {'user_id': user_id}
        return self.execute_query(query, params, False)
    def get_cards_of_deck(self, deck_id):
        query = "SELECT card_id FROM card_links WHERE deck_id = :deck_id"
        params = {'deck_id': deck_id}
        return self.execute_query(query, params, False)
    


    def user_exists_already(self, username=None, email=None):
        """Check if a user with given username and/or email already exists.
        Returns a dictionary with flags for each."""
        exists = {'username': False, 'email': False, 'any': False}
        if username or email:
            if username:
                username_query = "SELECT 1 FROM users WHERE username = :username"
                username_result = self.execute_query(username_query, {'username': username}, False)
                exists['username'] = len(username_result) > 0
            if email:
                email_query = "SELECT 1 FROM users WHERE email = :email"
                email_result = self.execute_query(email_query, {'email': email}, False)
                exists['email'] = len(email_result) > 0
            exists['any'] = exists['username'] or exists['email']
        return exists
    def register_user(self, username, email, server_hash, salt):
        query = 'INSERT INTO users(username, email, password_hash, salt) VALUES(:username, :email, :server_hash, :salt)'
        params = {'username': username, 'email': email, 'server_hash': server_hash, 'salt': salt}
        self.execute_query(query, params)

    def login_user(self, email, client_hashed_password):
        user_id = self.get_user_id_from_identifier(email, search_by_email=True)
        user = self.get_user_details(user_id, False)
        if user and check_password_hash(user['password_hash'], client_hashed_password + user['salt']):
            return True
        else:
            return False
    def get_user_id_from_identifier(self, identifier, search_by_email=True):
        """Returns the user_id (None if not found) from an identifier that is either the email (by default) or the username"""
        field = 'email' if search_by_email else 'username'
        query = f"SELECT id FROM users WHERE {field} = :identifier"
        user = self.execute_query(query, {'identifier': identifier}, False)
        return user[0]['id'] if user else None
    def get_user_details(self, user_id, privacy = True):
        """Gets the user details considering his user_id"""
        if privacy:
            query = "SELECT id, username, email, created_at FROM users WHERE id = :user_id"
        else:
            query = "SELECT * FROM users WHERE id = :user_id"
        user_details = self.execute_query(query, {'user_id': user_id}, False)
        return user_details[0] if user_details else None
    
    def lock_account(self, user_id):
        query = "UPDATE users SET is_locked = 1 WHERE id = :user_id"
        self.execute_query(query, {'user_id': user_id}, True)
    def unlock_account(self, user_id):
        query = "UPDATE users SET is_locked = 0 WHERE id = :user_id"
        self.execute_query(query, {'user_id': user_id}, True)
    def is_account_locked(self, user_id):
        query = "SELECT is_locked FROM users WHERE id = :user_id"
        result = self.execute_query(query, {'user_id': user_id}, False)
        return result and result[0]['is_locked']

    def has_multiple_failed_logins(self, user_id, hours, threshold):
        query = """
        SELECT COUNT(DISTINCT ip_address) AS unique_ips
        FROM failed_login_attempts
        WHERE user_id = :user_id AND last_failed_login > DATETIME('now', '-' || :hours || ' hours')
        """
        result = self.execute_query(query, {'user_id': user_id, 'hours': hours}, False)
        print(result)
        return result and result[0]['unique_ips'] >= threshold

    def get_log_attempts(self, user_id):
        """Gets all failed log attempts (for suspicious activity detection)"""
        query = "SELECT * from failed_login_attempts WHERE user_id = :user_id"
        params = {'user_id': user_id}
        return self.execute_query(query, params, False)
    
    def get_failed_attempts_for_ip(self, user_id, ip_address):
        query = """
            SELECT * FROM failed_login_attempts
            WHERE user_id = :user_id AND ip_address = :ip_address
        """
        result = self.execute_query(query, {'user_id': user_id, 'ip_address': ip_address}, False)
        return result[0] if result else None

    def increment_failed_attempts(self, user_id, ip_address):
        """Increases the failed attempts"""
        exists_query = "SELECT 1 FROM failed_login_attempts WHERE user_id = :user_id AND ip_address = :ip_address"
        exists = self.execute_query(exists_query, {'user_id': user_id, 'ip_address': ip_address}, False)
        if exists:
            query = "UPDATE failed_login_attempts SET attempts = attempts + 1, last_failed_login = CURRENT_TIMESTAMP WHERE user_id = :user_id AND ip_address = :ip_address"
        else:
            query = "INSERT INTO failed_login_attempts (user_id, ip_address, attempts, last_failed_login) VALUES (:user_id, :ip_address, 1, CURRENT_TIMESTAMP)"
        self.execute_query(query, {'user_id': user_id, 'ip_address': ip_address}, True)

    def reset_failed_attempts(self, user_id, ip_address):
        """Reset the failed attempts for a certain (user_id, ip_address)"""
        query = "UPDATE failed_login_attempts SET attempts = 0 WHERE user_id = :user_id AND ip_address = :ip_address"
        self.execute_query(query, {'user_id': user_id, 'ip_address': ip_address}, True)

