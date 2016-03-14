from Deck import Deck


class Shoe(object):
    """
        Holds multiple Deck objects
    """
    def __init__(self, decks=1):
        self.shoe = [Deck() for _ in xrange(decks)]
        for deck in self.shoe:
            for card in deck.cards:
                print card

'''test code'''
test = Shoe(2)