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



class Game():
    #deck
    #players