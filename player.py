import Card


class Player (object):
    def __init__(self, name='default', points =100):
        self.name = name
        # self.points = points
        self.hand = Hand()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,val):
        self._name = val

    #getter/setter for points

    def hit(self, card):
        self.hand.list.append(card)
        #update score
        self.hand.get_score()

    #def stand(self):
        # do nothing


class Hand(object):
    """
    collection of player's cards
    """
    def __init__(self):
        self._list = []
        self.score = 0

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, val):
        self._list = val

    # can only add to this list using obj.list.append
    def append(self, val):
        return self.list.append(val)

    def get_score(self):
        score_sum = 0
        ace = 0
        #print "get_score"
        #print len(self._list)
        for card in self._list:
            #print "card rank:" + str(card.rank)
            if card.is_ace():
                ace += 1
                #print "{0} aces".format(ace)
            score_sum += card.value

        for x in xrange(ace):
            if score_sum > 21:
                score_sum -= 10

        #print "{0} current score".format(score_sum)
        self.score = score_sum

'''
test_player = Player()
new_card = Card.Card(4, 'H')
test_player.hit(new_card)
new_card = Card.Card('A', 'H')
test_player.hit(new_card)
new_card = Card.Card(2, 'H')
test_player.hit(new_card)
new_card = Card.Card('A', 'H')
test_player.hit(new_card)


#print test_player.hand.list

#test_hand = Hand()
#test_hand.list.extend([1, 2])
#test.hit(new_card)
#print test_hand.list
'''