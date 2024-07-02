class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.value <= 8:
            return f'{self.value + 2} of {self.suit}'
        if self.value == 9:
            return f'Jack of {self.suit}'
        if self.value == 10:
            return f'Queen of {self.suit}'
        if self.value == 11:
            return f'King of {self.suit}'
        if self.value == 12:
            return f'Ace of {self.suit}'

    def rank(self, leadSuit):
        if self.suit != leadSuit:
            return 0
        return self.value
