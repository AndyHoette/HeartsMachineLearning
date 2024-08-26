from card import Card


class Turn:
    def __init__(self):
        self.cardsPlayed: list[Card] = []

    def cardPlayed(self, card: Card):
        self.cardsPlayed.append(card)

    def winner(self):
        leadSuit: str = self.cardsPlayed[0].suit
        winningCard: Card = self.cardsPlayed[0]
        for card in self.cardsPlayed[1:]:
            if card.suit == leadSuit:
                if winningCard < card:
                    winningCard = card
        return self.cardsPlayed.index(winningCard)

    def points(self):
        pointsForTrick: int = 0
        for card in self.cardsPlayed:
            pointsForTrick += card.pointValue()
        return pointsForTrick

    def clearCards(self):
        self.cardsPlayed = []

