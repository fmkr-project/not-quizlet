class Deck:
    """
    Class representing a set of cards
    """
    def __init__(self):
        self.id = None      # TODO
        self.name = ""      # TODO
        self.contents = []  # TODO discuss about the structure (dict ? (true) set ? list ?)


def create_deck(database, id, name):
    database.cursor().execute("""insert into decks (id, name) values (?, ?)""", (id, name))
    database.commit()