import db

"""Debug functions to delete before production"""

def sanitize_data(data: db.Database):
    """Clear everything in the db"""
    data.conn.execute("delete from cards;")
    data.conn.execute("delete from decks;")
    data.conn.execute("delete from users;")
    
    # Rebuild the database
    with open('res/create_database.sql') as sqlfile:
        script = sqlfile.read()
    data.execute_sql(script)