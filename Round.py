import random
from Turn import Turn
from player import Player


class Round:
    def __init__(self):
        self.turn = Turn()
        player0: Player = Player()
        player1: Player = Player()
        player2: Player = Player()
        player3: Player = Player()
        self.players: list[Player] = [player0, player1, player2, player3]

    def dealCards(self):
        deck: list[int] = list(range(52))
        random.shuffle(deck)
        for idx, player in enumerate(self.players):
            player.deal_cards(deck[idx * 13: (idx + 1) * 13])
            player.sort_hand()

    def showHand(self, player: Player):
        if player == self.players[0]:
            print("Your Hand: ")
        print(player, end='\n')

    def anyPlayersOver100(self):
        for player in self.players:
            if (player.points == 100):
                player.points = 50
            if (player.points > 100):
                return True
        return False

    def displayScores(self):
        winningPlayer: Player = self.players[0]
        isTie: bool = False
        for idx, player in enumerate(self.players, start=1):
            print(f"Player {idx}: {player.points}")
            if player.points < winningPlayer.points:
                isTie = False
                winningPlayer = player
            if player.points == winningPlayer.points:
                isTie = True
        if self.anyPlayersOver100():
            print("Game Over")

