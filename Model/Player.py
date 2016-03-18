# this import is only needed for testing code
DEBUG = False
if DEBUG:
    from Card import Card


class Player (object):
    def __init__(self, name='player', starting_points=100):
        self.name = name
        self.is_active = True
        self.points = starting_points  # persistent throughout games
        self.bet = 0
        self.hands = [Hand()] # player could have multiple hands if split

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, val):
        self.__points = int(val)

    @property
    def bet(self):
        return self.__bet

    @bet.setter
    def bet(self, val):
        """
        -check bet and make sure it wont set you broke
        -update score with removal of bet
        :param val:
        :return: current bet if valid else -1
        """
        bet = int(val)
        # make sure the bet does not make points go below 0
        valid_bet = self.points - bet
        #print "player" + str(valid_bet)
        if valid_bet < 0:
            # bet greater then player's points so not valid
            self.__bet = -1  # cant use False since you can bet 100% of your points
        else:
            self.points -= bet
            self.__bet = bet

    def hit(self, hand, card):
        """
        -this will place card in correct hand of current player
        -score will be updated
        :param hand: current hand object
        :param card: card that has been taken out of shoe
        :return: false if hand score is greater then 21
        """
        hand.cards.append(card)
        hand.score = 0  # number shouldnt matter just need to use as a setter

        if hand.score > 21:
            hand.is_bust = True
            hand.status = "loser"

        return hand.is_bust

    # TODO probably not a needed method
    def stand(self):
        # do nothing score should be up to date
        pass

    @property
    def hands(self):
        return self.__hands

    @hands.setter
    def hands(self, val):
        self.__hands = val

    def clear_hands(self):
        # print "cleared hands of {0} ".format(self.name)
        del self.hands[:]  # removes all hands
        self.hands.append(Hand())  # create new base hand


class Hand(object):
    """
    collection of player's cards
    """
    def __init__(self):
        self.cards = []
        self.score = 0  # TODO has to use _score since no setter for this property
        self.status = None
        self.is_bust = False

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, val):
        self.__cards = val

    def reset(self):
        self.__init__()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        score_sum = 0
        ace = 0
        #print "get_score"
        #print len(self._list)
        for card in self.cards:
            #print "card rank:" + str(card.rank)
            if card.is_ace:
                ace += 1
                #print "{0} aces".format(ace)
            score_sum += int(card.value)

        for x in xrange(ace):
            if score_sum > 21:
                score_sum -= 10

        #print "{0} current score".format(score_sum)
        self.__score = score_sum

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, val):
        self.__status = val

    def __str__(self):
        # return the cards in hand with correct visibility
        s = ''
        show_score = True

        for i in self.cards:
            s += i.__str__()
            if i.visibility is False:
                show_score = False

        # hide score if a card is face down
        if show_score:
            s += ' score: %d' % self.score
        return s

if DEBUG:
    test_player = Player()
    test_player.hands.append(Hand())

    print test_player.hands
    for index, elem in enumerate(test_player.hands):
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
