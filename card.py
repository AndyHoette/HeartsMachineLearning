class Card:
    def __init__(self, suit, value):
        self.suit: str = suit
        self.value: int = value

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

    def __lt__(self, other):
        suit_multipliers = {
            'Clubs': 0,
            'Diamonds': 1,
            'Spades': 2,
            'Hearts': 3
        }
        other_multiplier: int = suit_multipliers.get(other.suit)
        self_multiplier: int = suit_multipliers.get(self.suit)
        return self.value + self_multiplier*13 < other.value + other_multiplier*13

    def pointValue(self):
        if(self.suit == 'Diamonds' and self.value == 9):
            return -10
        if(self.suit == 'Spades' and self.value == 10):
            return 13
        if(self.suit == 'Hearts'):
            return 1

    def rank(self, leadSuit):
        if self.suit != leadSuit:
            return 0
        return self.value
