from Player import Player


class Dealer(Player):
    """
    Dealer is a special case of player
    differs:
        -starts with 1 card shown one hidden
        -hits if score < 17
            else stand
    """
    ''' TODO maybe call this instead of directly from shoe
    def deal(self, hidden=True):
        # get card from shoe and return it
        pass
    '''
    def hit(self, hand, card):
        # TODO need to not make this happen on the deal
        if len(self.hands[0].cards) >= 2:
            print "this happened:" + str(len(self.hands[0].cards))
            while self.hands[0].score <= 16:
                super(Dealer, self).hit(hand, card)
        else:
            if self.hands[0].score <= 16:
                print "score less then 17"
                super(Dealer, self).hit(hand, card)
