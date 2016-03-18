from Deck import Deck
import random

DEBUG = False


class Shoe(object):
    """
        Holds multiple Deck objects
    """
    def __init__(self, decks=1):
        self.shoe = [Deck() for _ in xrange(decks)]

    def draw(self, vis=True):
        # pick a card from a random deck in the shoe
        i = random.randint(0, len(self.shoe)-1)
        #print "draw card from deck {0}".format(i+1)
        card = self.shoe[i].draw()
        if vis:
            card.visibility = True
        return card

if DEBUG:
    '''test code'''
    print "------ Start Shoe test code -------"
    test = Shoe(2)
    print(test.draw())
    print "------ End Shoe test code -------"
