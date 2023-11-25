import pytest
import os
from pathlib import Path
from .database_test import Database_test

class Debug:
    @pytest.fixture(scope="class", params=["local", "remote"])
    def db_instance(self, request):
        db = Database_test(is_local=(request.param == "local"))
        yield db
        if db.session is not None:
            db.close()

    def test_connect(self, db_instance):
        db_instance.connect()
        assert db_instance.session is not None
    def test_close(self, db_instance):
        db_instance.close()
        assert db_instance.session is None

def run_tests():
    test_file_path = Path(__file__).parent / 'debug_test.py'
    print(test_file_path)
    pytest.main(['-v', str(test_file_path)])