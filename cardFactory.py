from card import Card


class CardFactory:
    def create_card(*args):
        newCard: Card = None
        if len(args) == 2:
            if args[1] <= 12:
                newCard = Card("Clubs", args[1])
            elif args[1] <= 25:
                newCard = Card("Diamonds", args[1]%13)
            elif args[1] <= 38:
                newCard = Card("Spades", args[1]%13)
            else:
                newCard = Card("Hearts", args[1]%13)
            return newCard
        else:
            newCard = Card(args[1], args[2])
        return newCard
