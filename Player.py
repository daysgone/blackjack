# this import is only needed for testing code
DEBUG = False
if DEBUG:
    from Card import Card


class Player (object):
    def __init__(self, name='player'):
        self._name = name

        # player could have multiple hands if split
        self.hand = [Hand()]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    # getter/setter for points

    def hit(self, hand, card):
        """
        this will place card in correct hand of current player
        score will be updated
        :param hand: index value of hand to add card to
        :param card: card that has been taken out of shoe
        :return:
        """
        for h in self.hand:
            h.list.append(card)
            h.score()

    #def stand(self):
        # do nothing

    def get_hand(self):
        return self.hand.list


class Hand(object):
    """
    collection of player's cards
    """
    def __init__(self):
        self._list = []
        self._score = 0

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, val):
        self._list = val

    def score(self):
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

        print "{0} current score".format(score_sum)
        self._score = score_sum
        return self._score

if DEBUG:
    test_player = Player()
    new_card = Card(4, 'H')
    test_player.hit(new_card)
    new_card = Card('A', 'H')
    test_player.hit(new_card)
    new_card = Card(2, 'H')
    test_player.hit(new_card)
    new_card = Card('A', 'H')
    test_player.hit(new_card)

    #test_player.hand[0].score()
    #print test_player.hand.list

    #test_hand = Hand()
    #test_hand.list.extend([1, 2])
    #test.hit(new_card)
    #print test_hand.list
