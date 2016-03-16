#CONTROLLER

from Player import Player
from Dealer import Dealer
from Shoe import Shoe

from Card import Card

#import View


class Game(object):
    def __init__(self, players, start_credit=100):
        self.dealer = Dealer()
        self.shoe = Shoe()
        self.players = [Player(player) for player in players]
        #print len(self.players)

    def hit(self, p, h):
        """
        hitting happens on a per hand basis
        :param p: player index
        :return: none
        """
        player = self.players[p]  # change from index to object
        hand = player.hand[h]
        player.hit(self.shoe.deal())
        print "{0}'s hand now contains {1}".format(player.name, player.hand[h].list[-1])

        self.check_score(player)

    def check_score(self, player):
        score = self.players[player].hand.get_score()
        if score > 21:
            #then bust
            print score
            return score

        else:
            print score
            return score

newGame = Game(['name'])
newGame.hit(0)
newGame.hit(0)
newGame.hit(0)
newGame.hit(0)
'''
for i in newGame.players[0].get_hand():
    print i
'''