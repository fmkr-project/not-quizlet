class Database:
    def __init__(self, object):
        self.database = object

    def create_deck(self, id, name):
        self.database.cursor().execute("""insert into decks (id, name) values (?, ?)""", (id, name))
        self.database.commit()