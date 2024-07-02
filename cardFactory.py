from card import Card


class CardFactory:
    def create_card(self, idx):
        newCard = None
        if idx <= 12:
            newCard = Card("Clubs", idx)
        elif idx <= 25:
            newCard = Card("Diamonds", idx%13)
        elif idx <= 38:
            newCard = Card("Spades", idx%13)
        else:
            newCard = Card("Hearts", idx%13)
        return newCard
