class Card:
    def __init__(self, id, frontSide, backSide, labels):
        self.id = id
        self.frontSide = frontSide
        self.backSide = backSide
        self.labels = labels.split(',')
