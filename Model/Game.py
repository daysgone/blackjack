#MODEL Modules
from Player import Player
from Dealer import Dealer
from Shoe import Shoe

DEBUG = False


class Game(object):
    def __init__(self):
        self.name = 'Blackjack'
        self.dealer = Dealer('Dealer', 0)
        self.players = None
        self.shoe = None

    def start_game(self, players, deck_size=1):
        self.players = [Player(player) for player in players]
        self.shoe = Shoe(deck_size)

    def quit_game(self):
        pass

    def place_bet(self, player, bet):
        """
        only accepts 0 < valid bets <= player.score
        will make player inactive if bet of 0 is placed
        :param player: current player
        :param bet: integer
        :return:
        """
        # bet only called on first hand of player
        player.bet = int(bet)

        if player.bet == 0:
            player.is_active = False
            return True
        elif player.bet == -1:
            return False
        else:
            return True

    def deal_cards(self, dealer_face=True):
        """
        will deal out 1 card to every player and dealer (default face up)
        """
        if len(self.players): # dont deal cards if no players left to play
            for player in self.players:
                # can only be one hand to start per player
                player.hit(player.hands[0], self.shoe.draw())

            # deal card to dealer
            self.dealer.hit(self.dealer.hands[0], self.shoe.draw(dealer_face))
        else:
            print "GAME: no players left to deal to should exit out of game here"

    def remove_players(self):
        # remove players from game since is_active is set to false: bet of 0, 0 points left
        new_players = []
        for p in self.players:
            if p.is_active:
                new_players.append(p)
            else:
                print "GAME: removed {0}".format(p.name)
        self.players = new_players

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
        cur_hand = cur_player.hands[hand]
        # TODO maybe make dealer deal instead of draw from shoe directly?
        bust = cur_player.hit(cur_hand, self.shoe.draw(True))
        # print "{0} now added to {1}'s hand ".format(cur_player.hand[hand].list[-1], cur_player.name )

        return bust, cur_hand

    ''' this should only be a view method
    @staticmethod
    def stand(player, hand):
        msg = player.name + " stands with a score of " + str(hand.score)
        return msg
    '''

    @staticmethod
    def show_card(player, hand=0):
        """
        first card in deck is usualy not shown, this will show it
        :param player: player to flip card
        :param hand: hand to flip card
        :return: last card
        """
        for card in player.hands[hand].cards:
            card.visibility = True

    ''' use again when insurance feature added
    def check_dealer_card_ace(self):
        # return True if 2nd card is an ace
        # needed to check for insurance
        if self.dealer.hands[0].cards[1].rank == 'A':
            return True
        else:
            return False
    '''
    def check_winner(self):
        # if dealer busts
        if self.dealer.hands[0].is_bust:
            # check players for bust
            for p in self.players:
                for h in p.hands:
                    if not h.is_bust:
                        h.status = "win"
        else:
            for p in self.players:
                self.compare(p, self.dealer)

    @staticmethod
    def collect_winnings(player):
        for h in player.hands:
            if h.status == "win":
                player.points = player.bet * 2
            elif h.status == "tie":
                player.points = player.bet
            else:
                if not player.points:
                    player.is_active = False

    def clear_hands(self):
        # reset all hands of players for start of new game
        for p in self.players:
            p.clear_hands()
        self.dealer.clear_hands()

    @staticmethod
    def compare(player, dealer):
        dealer_score = dealer.hands[0].score
        # compare score to player
        #print "dealer: {0}, {1}: {2}".format(dealer_score, player.name, player.hand[0].score)
        for h in player.hands:
            if not h.is_bust:
                if h.score > dealer_score:
                    h.status = "wins"
                    player.points += (player.bet * 2)
                    dealer.hands[0].status = "loses"
                elif h.score == dealer_score and not dealer.hands[0].is_bust:
                    h.status = "ties"
                    player.points += player.bet
                    dealer.hands[0].status = "ties"
                else:
                    h.status = "loses"
                    dealer.hands[0].status = "wins"


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
    #show current hands
    for p in players:
        print p.name + " currently has " + str(p.hands[0])

    print "Dealer currently has " + str(dealer.hands[0])
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
