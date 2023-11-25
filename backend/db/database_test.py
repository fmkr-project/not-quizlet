from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash
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

class Database_test:
    def __init__(self, is_local = USE_LOCAL_DATABASE_ENV, is_test = True):
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
        - Local = {self.is_local}>"""
        else:
            s = f"""<Database object:
        - Test Database = {self.is_test},
        - Connection = {is_connected},
        - Host = {AWS_DATABASE_ENDPOINT},
        - Port = {AWS_DATABASE_PORT},
        - User = {AWS_DATABASE_USERNAME},
        - Database = {AWS_DATABASE_NAME}>"""
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
                result = self.session.execute(text(query), params).fetchall()
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
            # In SQLAlchemy, you need to execute each statement separately
            for statement in sql_script.split(';'):
                # Skipping empty statements (useful when script contains newline characters)
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

    def create_card(self, front_side, back_side):
        """Create a new card"""
        query = "INSERT INTO cards (front_side, back_side) VALUES (:front_side, :back_side)"
        params = {'front_side': front_side, 'back_side': back_side}
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
    
    def create_deck(self, name, description):
        """Create a new deck with a name and a description"""
        query = "INSERT INTO decks (name, description) VALUES (:name, :description)"
        params = {'name': name, 'description': description}
        self.execute_query(query, params)
    def modify_deck(self, deck_id, name, description):
        """Modify the deck with the given ID"""
        query = "UPDATE decks SET name = :name, description = :description WHERE id = :deck_id"
        params = {'name': name, 'description': description, 'deck_id': deck_id}
        self.execute_query(query, params)
    def delete_deck(self, deck_id):
        """Delete the deck with the given ID"""
        query = "DELETE FROM decks WHERE id = :deck_id"
        params = {'deck_id': deck_id}
        self.execute_query(query, params)
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
        return self.execute_query(query, params)

    def login_user(self, email, client_hashed_password):
        user = self.get_user_id_from_identifier(email, search_by_email=True)
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
    def get_user_details(self, user_id):
        """Gets the user details considering his user_id"""
        query = "SELECT id, username, email, created_at FROM users WHERE id = :user_id"
        user_details = self.execute_query(query, {'user_id': user_id}, False)
        return user_details[0] if user_details else None