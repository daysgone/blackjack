# this import is only needed for testing code
DEBUG = False
if DEBUG:
    from Card import Card


class Player (object):
    def __init__(self, name='player'):#, points=0):
        self.name = name
        #self.points = points
        # player could have multiple hands if split
        self.hand = [Hand()]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    '''
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, val):
        # make sure the bet does not make pool go below 0
        temp_points = self._points + val
        if temp_points < 0:
            return False
        else:
            self._points = temp_points
            return True
    '''

    def hit(self, hand, card):
        """
        -this will place card in correct hand of current player
        -score will be updated
        :param hand: current hand object
        :param card: card that has been taken out of shoe
        :return: false if hand score is greater then 21
        """
        hand.list.append(card)
        hand.update_score()

        if hand.score > 21:
            hand.is_bust = True
            hand.status = "lost"

        return hand.is_bust

    # TODO probably not a needed method
    def stand(self):
        # do nothing score should be up to date
        pass

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, val):
        self._hand = val


class Hand(object):
    """
    collection of player's cards
    """
    def __init__(self):
        self.list = []
        self._score = 0  # TODO has to use _score since no setter for this property
        self.status = None
        self.is_bust = False

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, val):
        self._list = val

    @property
    def score(self):
        return self._score

    # TODO would like to  figure out how to make this a setter attribute
    def update_score(self):
        score_sum = 0
        ace = 0
        #print "get_score"
        #print len(self._list)
        for card in self.list:
            #print "card rank:" + str(card.rank)
            if card.is_ace:
                ace += 1
                #print "{0} aces".format(ace)
            score_sum += int(card.value)

        for x in xrange(ace):
            if score_sum > 21:
                score_sum -= 10

        #print "{0} current score".format(score_sum)
        self._score = score_sum
        return self._score

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        self._status = val

    def __str__(self):
        # return the cards in hand with correct visibility
        s = ''
        show_score = True

        for i in self.list:
            s += i.__str__()
            if i.visibility is False:
                show_score = False

        # hide score if a card is face down
        if show_score:
            s += ' score: %d' % self.score
        return s

if DEBUG:
    test_player = Player()
    test_player.hand.append(Hand())

    print test_player.hand
    for index, elem in enumerate(test_player.hand):
        print "Hand %d" % index
        new_card = Card(4, 'H')
        test_player.hit(elem, new_card)

    '''
    new_card = Card(2, 'H')
    test_player.hit(new_card)
    new_card = Card('A', 'H')
    test_player.hit(new_card)
    '''
    #test_player.hand[0].score()
    #print test_player.hand.list

    #test_hand = Hand()
    #test_hand.list.extend([1, 2])
    #test.hit(new_card)
    #print test_hand.list
