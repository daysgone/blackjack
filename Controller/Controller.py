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
        # players stay the same
        self.view.clear()
        # clear out player hands
        self.game.clear_hands()
        self.start_game()

    def start_game(self):
        self.bet()
        self.deal()

        # if dealer's face up card is an Ace players can purchase insurance for half their bet
        if self.game.check_dealer_card_ace():
            self.view.show_msg("dealer shows an ace, purchase insurance?")
            # would loop through all players hands and ask for insurance

        # flip over 1st dealt Dealer card
        self.view.show_msg("dealer flips over card")
        self.game.show_card(self.game.dealer)

        # if dealer shows blackjack take orig bets from those who did not buy insurance

        # if insurance not bought only players with blackjack keep orig bet

        self.play()

        if self.view.new_game():
            self.new_game()

    def bet(self):
        for p in self.game.players:
            valid_bet = False
            # keeps asking for bet till valid
            # TODO needs an exit case of 0, in which player would be removed from game
            while not valid_bet:
                valid_bet = self.game.place_bet(p, self.view.get_bet(p))

    def deal(self):
        # wait for players to make bets
        if self.view.deal():
            self.view.clear()
            # deal cards
            self.game.deal_cards()

            # update view with dealt cards
            for p in self.game.players:
                self.view.update_hand(p)

            self.view.update_hand(self.game.dealer)

    # TODO i think some of this code should be in model
    def play(self):
        # start with first player, hit until bust or stand, continue with other players
        busted = 0
        for p in self.game.players:
            keep_going = True
            while keep_going:
                self.view.update_hand(self.game.dealer)
                self.view.update_hand(p)

                if self.view.choose():
                    self.view.clear()
                    self.view.hit(p)

                    bust, hand = self.game.hit(p)

                    if bust:
                        self.view.busted(p, hand)
                        busted += 1
                        keep_going = False
                else:
                    self.view.clear()
                    self.view.stand(p)
                    keep_going = False

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
            else:
                for p in self.game.players:
                    if not p.hands[0].is_bust:
                        # need to check for tie case
                        self.view.status(p)

        else:
            self.view.status(self.game.dealer)

# if dealer under 21 pay players with a higher score
# take money from those with lower
# tie with player, refund bet



