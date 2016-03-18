#MODEL Modules
from Player import Player
from Dealer import Dealer
from Shoe import Shoe

#import View

DEBUG = False


class Game(object):
    def __init__(self, players, deck_size=1):
        self.dealer = Dealer('Dealer')
        self.players = [Player(player) for player in players]
        self.shoe = Shoe(deck_size)

    def place_bets(self):
        pass

    def deal_cards(self):
        """
        will deal out 1 card to every player and dealer face down
        will deal out 1 card to every player and dealer face up
        """
        # deal 1 card to every player and dealer face down
        for player in self.players:
            # can only be one hand to start per player
            # TODO should be first card dealt face down, but not doing that
            player.hit(player.hand[0], self.shoe.draw(True))

        # deal card to dealer
        self.dealer.hit(self.dealer.hand[0], self.shoe.draw())

        # deal 1 card to every player and dealer face up
        for player in self.players:
            # can only be one hand to start per player
            player.hit(player.hand[0], self.shoe.draw(True))

        # deal card to dealer
        self.dealer.hit(self.dealer.hand[0], self.shoe.draw(True))

    @staticmethod
    def insurance(player, taken=False):
        """
        insurance is only offered to players if the dealer has an Ace showing
        on the initial deal
        :param player: individual player
        :param taken: True only if the player decided to take insurance
        """
        pass

    def hit(self, player, hand=0):
        """
        hitting happens on a per hand basis
        :param player: player object
        :param hand: hand index
        :return: returns False if the hit caused the player to bust
        """
        # cur_player = self.players[player]  # change from index to object
        cur_player = player
        cur_hand = cur_player.hand[hand]
        bust = cur_player.hit(cur_hand, self.shoe.draw(True))
        # print "{0} now added to {1}'s hand ".format(cur_player.hand[hand].list[-1], cur_player.name )

        return bust, cur_hand
        '''
        if cur_hand.is_bust:
            #print "{0} busted".format(cur_player.name)
            return True
        else:
            return False
        '''

    @staticmethod
    def stand(player, hand):
        print player.name + " stands with a score of " + str(hand.score)
        return True

    @staticmethod
    def show_card(player, hand=0):
        for card in player.hand[hand].list:
            card.visibility = True

    @staticmethod
    def compare(player, dealer):
        verdict = None
        dealer_score = dealer.hand[0].score
        # compare score to player
        print "dealer: {0}, {1}: {2}".format(dealer_score, player.name, player.hand[0].score)
        for h in player.hand:
            if not h.is_bust:
                if h.score > dealer_score:
                    print "win"
                elif h.score == dealer_score:
                    print "tie"
                else:
                    print "lost"
            else:
                print "already busted cant win"

    def check_winner(self):
        for p in self.players:
            self.compare(p, self.dealer)





#UI = View()











if DEBUG:
    blackjack = Game(['player1', 'player2'])
    dealer = blackjack.dealer
    players = blackjack.players

    # place bets
    for p in players:
        blackjack.place_bets()
        pass

    # deal cards
    blackjack.deal_cards()

    # if dealers first card is an Ace
        # ask players if they want insurance
            # half of orig bet

    # dealer flip over 2nd card
    blackjack.show_card(dealer)

    # if blackjack take orig bets from those who did not buy insurance
    # if insurance not bough only players with blackjack keep orig bet

    # start with first player and hit until bust or they stay
    #for p in players:

    # over 21 then bust

    # continue with all other players

    # dealer hits if score is less then 16
    # stay if above

    # if dealer busts all players win
    # if dealer under 21 pay players with a higher score
    # take money from those with lower
    # tie with player, refund bet

    # start new hand

    # show cards in players hand
    '''
    for p in blackjack.players:
        print p.name + 's hand ' + str(p.hand[0])

    print blackjack.dealer.name + 's hand ' + str(blackjack.dealer.hand[0])

    for p in blackjack.players:
        if blackjack.hit(p, 0):
            print p.hand[0]
        else:
            print p.name + ' busted'
    blackjack.stand(blackjack.players[0], blackjack.players[0].hand[0])
    #print blackjack.dealer.name
    print blackjack.hit(blackjack.dealer, 0)
    print blackjack.dealer.hand[0]
    '''
