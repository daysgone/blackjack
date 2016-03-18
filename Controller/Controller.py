class Controller(object):
    def __init__(self, game, view):
        self.game = game
        self.view = view
        self.initialize()

    def initialize(self):
        # get player names from view and put in model
        self.game.start_game(self.view.set_players(), 2)

        self.start_game()

    def start_game(self):
        self.bet()
        self.deal()

        # if card shown on dealer is an Ace players can purchase insurance for half their bet
        # flip over 2nd Dealer card
        self.game.show_card(self.game.dealer)

        # if blackjack take orig bets from those who did not buy insurance
        # if insurance not bought only players with blackjack keep orig bet

        self.play()

    def bet(self):
        pass

    def deal(self):
        # wait for players to make bets
        if self.view.deal():
            self.view.clear()
            # deal cards
            self.game.deal_cards()

            # update view with dealt cards
            for p in self.game.players:
                self.view.update_hand(p)

            # TODO add this back in if insurance feature is added
            # self.view.update_hand(self.game.dealer)



    # TODO i think some of this code should be in model
    def play(self):
        busted = 0
        # start with first player, hit until bust or stand, continue with other players
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

                # see if anyone else won
                #self.game.check_winner()
                for p in self.game.players:
                    if not p.hand[0].is_bust:
                        self.view.winner(p)
                #winners = self.game.check_winner()

                #self.view.show_winners(winners)
            else:
                #self.game.check_winner()
                for p in self.game.players:
                    if not p.hand[0].is_bust:
                        self.view.winner(p)

        else:
            self.view.winner(self.game.dealer)

# if dealer under 21 pay players with a higher score
# take money from those with lower
# tie with player, refund bet



