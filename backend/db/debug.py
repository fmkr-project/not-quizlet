import pytest
import os
from pathlib import Path
from .database import Database, DB_TEST_PATH, SQLAlchemyError
class TestDatabase():
    @pytest.fixture(scope="class", params=["local"])
    def db_instance(self, request):
        db = Database(is_local=(request.param == "local"), is_test = True)
        yield db
        if db.session is not None:
            db.close()

    def test_connect(self, db_instance : Database):
        db_instance.connect()
        assert db_instance.session is not None
    def test_close(self, db_instance : Database):
        db_instance.close()
        assert db_instance.session is None

    def test_execute_sql(self, db_instance : Database):
        sql_script_path = DB_TEST_PATH
        try:
            print(sql_script_path)
            db_instance.execute_sql(sql_script_path)
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised while executing SQL script")
            
    def test_create_card(self, db_instance: Database):
        front_side = "Test Front"
        back_side = "Test Back"
        try:
            db_instance.create_card(front_side, back_side)
            query = "SELECT * FROM cards WHERE front_side = :front_side AND back_side = :back_side"
            result = db_instance.execute_query(query, {'front_side': front_side, 'back_side': back_side}, False)
            assert len(result) > 0, "Card was not created"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during card creation")
    def test_modify_card(self, db_instance: Database):
        front_side = "Original Front"
        back_side = "Original Back"
        new_front_side = "Modified Front"
        new_back_side = "Modified Back"
        try:
            db_instance.create_card(front_side, back_side)
            query = "SELECT id FROM cards WHERE front_side = :front_side AND back_side = :back_side"
            result = db_instance.execute_query(query, {'front_side': front_side, 'back_side': back_side}, False)
            card_id = result[0][0]
            db_instance.modify_card(card_id, new_front_side, new_back_side)
            verify_query = "SELECT * FROM cards WHERE id = :card_id"
            modified_card = db_instance.execute_query(verify_query, {'card_id': card_id}, False)
            assert modified_card[0]['front_side'] == new_front_side and modified_card[0]['back_side'] == new_back_side, "Card was not modified correctly"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during card modification")
    def test_delete_card(self, db_instance: Database):
        front_side = "Test Front for Deletion"
        back_side = "Test Back for Deletion"
        try:
            db_instance.create_card(front_side, back_side)
            query = "SELECT id FROM cards WHERE front_side = :front_side AND back_side = :back_side"
            result = db_instance.execute_query(query, {'front_side': front_side, 'back_side': back_side}, False)
            card_id = result[0][0]
            db_instance.delete_card(card_id)
            verify_query = "SELECT * FROM cards WHERE id = :card_id"
            deleted_card = db_instance.execute_query(verify_query, {'card_id': card_id}, False)
            assert len(deleted_card) == 0, "Card was not deleted"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during card deletion")

    def test_create_deck(self, db_instance: Database):
        name = "Test Deck"
        description = "Test Description"
        try:
            db_instance.create_deck(name, description)
            query = "SELECT * FROM decks WHERE name = :name AND description = :description"
            result = db_instance.execute_query(query, {'name': name, 'description': description}, False)
            assert len(result) > 0, "Deck was not created"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during deck creation")
    def test_modify_deck(self, db_instance: Database):
        original_name = "Original Deck"
        original_description = "Original Description"
        new_name = "Modified Deck"
        new_description = "Modified Description"

        try:
            db_instance.create_deck(original_name, original_description)
            query = "SELECT id FROM decks WHERE name = :name AND description = :description"
            result = db_instance.execute_query(query, {'name': original_name, 'description': original_description}, False)
            deck_id = result[0][0]
            db_instance.modify_deck(deck_id, new_name, new_description)
            verify_query = "SELECT * FROM decks WHERE id = :deck_id"
            modified_deck = db_instance.execute_query(verify_query, {'deck_id': deck_id}, False)
            assert modified_deck[0]['name'] == new_name and modified_deck[0]['description'] == new_description, "Deck was not modified correctly"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during deck modification")
    def test_delete_deck(self, db_instance: Database):
        name = "Test Deck for Deletion"
        description = "Test Description for Deletion"
        try:
            db_instance.create_deck(name, description)
            query = "SELECT id FROM decks WHERE name = :name AND description = :description"
            result = db_instance.execute_query(query, {'name': name, 'description': description}, False)
            deck_id = result[0][0]
            db_instance.delete_deck(deck_id)
            verify_query = "SELECT * FROM decks WHERE id = :deck_id"
            deleted_deck = db_instance.execute_query(verify_query, {'deck_id': deck_id}, False)
            assert len(deleted_deck) == 0, "Deck was not deleted"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during deck deletion")
    def test_switch_deck_favorite_state(self, db_instance: Database):
        username = "testuser"
        email = "testuser@example.com"
        password_hash = "dummy_hash"
        salt = "dummy_salt"

        try:
            # Insert a test user directly
            insert_user_query = "INSERT INTO users (username, email, password_hash, salt) VALUES (:username, :email, :password_hash, :salt)"
            db_instance.execute_query(insert_user_query, {'username': username, 'email': email, 'password_hash': password_hash, 'salt': salt})

            # Retrieve the user ID
            user_query = "SELECT id FROM users WHERE username = :username"
            user_result = db_instance.execute_query(user_query, {'username': username}, False)
            user_id = user_result[0][0]

            # Create and retrieve a deck
            name = "Test Deck for Favorite"
            description = "Test Description for Favorite"
            db_instance.create_deck(name, description)
            deck_query = "SELECT id FROM decks WHERE name = :name AND description = :description"
            deck_result = db_instance.execute_query(deck_query, {'name': name, 'description': description}, False)
            deck_id = deck_result[0][0]

            # Link the deck with the user
            link_query = "INSERT INTO users_links (user_id, deck_id, favorite_tag) VALUES (:user_id, :deck_id, 0)"
            db_instance.execute_query(link_query, {'user_id': user_id, 'deck_id': deck_id})

            # Switch favorite state
            success = db_instance.switch_deck_favorite_state(user_id, deck_id)
            assert success, "Failed to switch the favorite state of the deck"

            # Verify the switch
            verify_query = "SELECT favorite_tag FROM users_links WHERE user_id = :user_id AND deck_id = :deck_id"
            favorite_state = db_instance.execute_query(verify_query, {'user_id': user_id, 'deck_id': deck_id}, False)
            assert favorite_state is not None and favorite_state[0][0] == 1, "Favorite state was not switched correctly"
        except SQLAlchemyError:
            pytest.fail("SQLAlchemyError was raised during switching deck favorite state")
        finally:
            # Clean up: delete the test user and deck
            delete_user_query = "DELETE FROM users WHERE username = :username"
            delete_deck_query = "DELETE FROM decks WHERE name = :name"
            db_instance.execute_query(delete_user_query, {'username': username})
            db_instance.execute_query(delete_deck_query, {'name': name})
def run_tests():
    test_file_path = Path(__file__).parent / 'debug.py'
    print(test_file_path)
    pytest.main(['-v', str(test_file_path)])