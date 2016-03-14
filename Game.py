import Deck
import Player
import Dealer


class Game():
    def __init__(self, players, start_credit=100):
        self.dealer = Dealer()
        self.deck = Deck()
        self.players = [Player(player,start_credit)} for player in players]