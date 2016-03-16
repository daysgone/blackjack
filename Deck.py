from Card import *
import random


class Deck(object):
    """
    collection of cards default deck does not include jokers
    """
    def __init__(self):
        # change deck size by number of suites and ranks in the external files
        self.cards = [Card(rank, suite) for suite in Suites.SUITES for rank in Ranks.RANKS]
        self.shuffle()

    def __str__(self):
        print ','.join(str(p) for p in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        # returns last item of list by default
        return self.cards.pop()

    def length(self):
        return len(self.cards)

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

'''test
print "-----Start Deck module test -----"
test = Deck()
new_card = test.choose()
print test.cards
print test.length()
print new_card
print "-----End Deck module test ------"
'''