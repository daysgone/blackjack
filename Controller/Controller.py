import time

class Controller(object):
    def __init__(self, game, view):
        self.game = game
        self.view = view
        self.initialize()

    def initialize(self):
        # get player names from view and put in model
        self.game.start_game(self.view.set_players(), 8)

        self.start_game()

    def new_game(self):
        if len(self.game.players):
            # players stay the same
            self.view.clear()
            # clear out player hands
            self.game.clear_hands()
            self.start_game()

    def start_game(self):
        '''
        # show current points for players
        for p in self.game.players:
            # make this a unique function
            self.view.show_msg("{0} currently has {1} points ".format(p.name, p.points))
        '''

        self.bet()

        if self.deal():  # only false if no players left

            ''' TODO
            # if dealer's face up card is an Ace players can purchase insurance for half their bet
            if self.game.check_dealer_card_ace():
                self.view.show_msg("dealer shows an ace, purchase insurance?")
                time.sleep(2)
                # would loop through all players hands and ask for insurance
                # insurance would be removed from points

            # flip over 1st dealt Dealer card
            # makes more sense if insurance is used
            self.view.show_msg("dealer flips over card")
            time.sleep(2)
            self.view.clear()
            self.game.show_card(self.game.dealer)

            # if dealer has blackjack
            #   # take bets from players who didn't buy insurance or hand is blackjack
            # players with active bets would still continue to play
            '''
            self.play()

            if self.view.new_game():
                self.new_game()

    def bet(self):
        for p in self.game.players:
            valid_bet = False
            # keeps asking for bet till valid one used
            while not valid_bet:
                valid_bet = self.game.place_bet(p, self.view.get_bet(p))
            self.view.clear()

        self.game.remove_players()  # strip out players that bet 0

    def deal(self):
        if len(self.game.players):

            self.view.show_msg("Dealer is dealing cards")  # TODO put this in view?
            time.sleep(2)
            self.view.clear()

            # this should be used with insurance added
            # self.game.deal_cards(False)  # deal cards, dealer's face down

            self.game.deal_cards(True)  # deals cards, dealer's face up
            self.game.deal_cards(True)  # deals cards, dealer's face up

            # update view with dealt cards
            for p in self.game.players:
                self.view.update_hand(p)

            self.view.update_hand(self.game.dealer)
            time.sleep(5)
            return True
        else:
            return False

    # TODO i think some of this code should be in model
    def play(self):
        # start with first player, hit until bust or stand, continue with other players
        busted = 0
        for p in self.game.players:
            keep_going = True
            while keep_going:
                self.view.clear()
                self.view.update_hand(self.game.dealer)
                self.view.update_hand(p)

                if self.view.choose():
                    self.view.move(p, ' hits ')
                    #self.view.clear()

                    bust, hand = self.game.hit(p)

                    if bust:
                        self.view.busted(p, hand)
                        busted += 1
                        keep_going = False
                else:
                    #self.view.clear()
                    self.view.move(p, ' stands ')

                    keep_going = False
                time.sleep(2)

        # if both players bust then no need to have dealer hit
        if busted != len(self.game.players):
            # print "both players did not bust"
            # dealer hits if score is less then 16
            bust, hand = self.game.hit(self.game.dealer)
            self.view.update_hand(self.game.dealer, hand)

            self.game.check_winner()

            if bust:
                self.view.busted(self.game.dealer)
                # see if anyone won
                for p in self.game.players:
                    if not p.hands[0].is_bust:
                        self.view.status(p)
                        self.game.collect_winnings(p)
            else:
                for p in self.game.players:
                    if not p.hands[0].is_bust:
                        # need to check for tie case
                        self.view.status(p)
                        self.game.collect_winnings(p)

        else:
            self.game.dealer.hands[0].status = 'wins'
            self.view.status(self.game.dealer)

# if dealer under 21 pay players with a higher score
# take money from those with lower
# tie with player, refund bet



