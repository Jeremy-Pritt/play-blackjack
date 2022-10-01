class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value

    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.val)
