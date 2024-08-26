import random
from card import Card
from player import Player
from cardFactory import CardFactory

cardMap = {
    "Clubs": {},
    "Diamonds": {},
    "Spades": {},
    "Hearts": {}
}
cf: CardFactory = CardFactory()
deck: list[Card] = []
for key in cardMap.keys():
    for i in range(13):
        newCard: Card = cf.create_card(key,i)
        deck.append(newCard)
        if i <= 8:
            cardMap[key][i+2] = newCard
        if i == 9:
            cardMap[key]["Jack"] = newCard
        if i == 10:
            cardMap[key]["Queen"] = newCard
        if i == 11:
            cardMap[key]["King"] = newCard
        if i == 12:
            cardMap[key]["Ace"] = newCard
PlayerTurn: int = 0
cardsPlayed: list[Card] = []
player0: Player = Player()
player1: Player = Player()
player2: Player = Player()
player3: Player = Player()
players: list[Player] = [player0, player1, player2, player3]
random.shuffle(deck)
for idx, player in enumerate(players):
    player.add_cards(deck[0+13*idx:13+13*idx])
    player.sort_hand()
print("Your Hand: ")
print(player0, end='\n')
for idx, player in enumerate(players):
    if player.has_card(cardMap["Clubs"][2]):
        print("True Reached")
        cardsPlayed.append(player.play_card(cardMap["Clubs"][2]))
        PlayerTurn = idx
        break
