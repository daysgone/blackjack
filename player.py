import random

class Player (object):
    def __init__(self):
        #cash
        #hand
        #get cash
        #change cash

    def getName(self):
    def hit(self):
    def stand(self):

#dealer is subclass of player


class Hand():
    """
    collection of cards
    """
    def __init__(self):
        # init empty list of cards
    def draw(self,deck):
        # draw from deck and put in hand
    def discard(self,deck):
        # return card to deck

    @property
    def value(self):
        # logic values

class Deck():
    """
    main collection of cards to be delt from
    """
    def __init__(self):
        # initialize deck with x number of cards
        self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
    def shuffle(self):
        # randomize position of cards
        random.shuffle(self.cards)

    def nextCard(self):
        #return next card in deck
    def getDeck(self):
        #return current cards in deck(list)

class Game():
    #deck
    #players