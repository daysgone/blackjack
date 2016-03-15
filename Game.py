#CONTROLLER

import Shoe
import Player
import Dealer


class Game(object):
    def __init__(self, players, start_credit=100):
        self.dealer = Dealer.Dealer()
        self.shoe = Shoe.Shoe()
        self.players = [Player.Player(player, start_credit) for player in players]
        #print len(self.players)

    def hit(self, player):
        card_to_deal = self.shoe.shoe[0].choose()
        print card_to_deal
        self.players[player].hit(card_to_deal)
        print self.players[player].hand.list[-1]
newGame = Game(['name'])
newGame.hit(0)
newGame.hit(0)
newGame.hit(0)
newGame.hit(0)
