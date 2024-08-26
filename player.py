from cardFactory import CardFactory
from card import Card


class Player:
    def __init__(self):
        self.hand = []

        self.points = 0

    def __str__(self):
        return '\n'.join(str(card) for card in self.hand)

    def add_cards(self, cards):
        for card in cards:
            self.hand.append(card)

    def sort_hand(self):
        self.hand.sort()

    def has_card(self, card):
        return card in self.hand

    def play_card(self, card):
        self.hand.remove(card)
        return card

    def addPoints(self, val):
        self.points += val
        return self.points
