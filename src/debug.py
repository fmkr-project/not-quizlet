import db

"""Debug functions to delete before production"""

def clear_data(data: db.Database):
    """Clear everything in the db"""
    data.conn.execute("drop table cards;")
    data.conn.execute("drop table decks;")
    data.conn.execute("drop table users;")
    
    # Rebuild the database
    with open('res/create_database.sql') as sqlfile:
        script = sqlfile.read()
    data.execute_sql(script)

def run_tests(data: db.Database):
    return