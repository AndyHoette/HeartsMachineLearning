from cardFactory import CardFactory
class Player:
    def __init__(self):
        self.hand = []
        self.cf = CardFactory()

    def __str__(self):
        return '\n'.join(str(card) for card in self.hand)
    def add_card(self, card):
        (self.hand).append(card)

    def deal_cards(self, idxs):
        for idx in idxs:
            card = self.cf.create_card(idx)
            self.add_card(card)
