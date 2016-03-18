from Card import *
import random

DEBUG = False


class Deck(object):
    """
    collection of cards default deck does not include jokers
    """
    def __init__(self):
        # change deck size by number of suites and ranks in the external files
        self.cards = [] #[Card(rank, suite) for suite in SUITES for rank in RANKS]
        self.shuffle()

    def __str__(self):
        return ','.join(str(p) for p in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        # returns last item of list by default
        return self.cards.pop()

    @property
    def cards(self):
        # return cards in current deck
        return self._cards

    @cards.setter
    def cards(self, val):
        self._cards = [Card(rank, suite) for suite in SUITES for rank in RANKS]

''' not needed if i just pop off list
    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, val):
        self.length = val
'''

''' Do we care about listing removed cards in deck?
    def get_deck(self):
        return
        #return current cards in deck(list)
'''

    # TODO do i need to keep track of already used cards?
    # def get_picked(self):

if DEBUG:
    print "-----Start Deck module test -----"
    test = Deck()
    print len(test.cards)
    new_card = test.draw()
    print len(test.cards)
    print new_card
    print "-----End Deck module test ------"
