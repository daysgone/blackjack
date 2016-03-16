from Deck import Deck
import random


class Shoe(object):
    """
        Holds multiple Deck objects
    """
    def __init__(self, decks=1):
        self.shoe = [Deck() for _ in xrange(decks)]
        '''
        for deck in self.shoe:
            for card in deck.cards:
                print card
        '''
    def deal(self):
        # pick a card from a random deck in the shoe
        i = random.randint(0, len(self.shoe)-1)
        print "picked card from deck {0}".format(i+1)
        return self.shoe[i].get_card()


'''test code
print "------ Start Shoe test code -------"
test = Shoe(2)
print(test.deal())
print "------ End Shoe test code -------"
'''