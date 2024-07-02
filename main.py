import random
from player import Player

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
players = [player1, player2, player3, player4]
deck = list(range(52))
random.shuffle(deck)
for idx, player in enumerate(players):
    player.deal_cards(sorted(deck[idx * 13: (idx + 1) * 13]))
print("Your Hand: ")
print(player1, end='\n')