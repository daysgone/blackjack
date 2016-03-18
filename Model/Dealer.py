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
        if hand.score >= 17:
            print "dealer cannot hit"
            self.stand()
        else:
            return super(Dealer, self).hit(hand, card)
