import os

from Model.Game import Game


class UI(object):
    def __init__(self):
        self.clear()
        self.players = []
        self.dealer = 'Dealer'

    @staticmethod
    def clear():
        os.system('clear')# linux/osx
        #os.system('cls') # windows

    def set_players(self):
        """
        get player names for controller
        :return: list of player names
        """
        prompt = int(raw_input("How many players? : "))
        self.clear()

        for n in xrange(1, prompt+1):
            self.players.append(raw_input("Please enter Player{0}'s name? : ".format(n)))
            self.clear()
        return self.players

    @staticmethod
    def new_game():
        # TODO need to capture if another input is entered
        answer = raw_input("\t\tNew Game? (Y,N) : ")
        if answer == 'N' or answer == 'n' or answer == "no":
            return False
        else:
            return True

    @staticmethod
    def deal():
        # TODO do somethign better here
        answer = raw_input("\t\tReady to Deal?")
        return True

    @staticmethod
    def update_hand(player, hand=0):
        if isinstance(hand, (int, long)):
            print player.name + "'s hand " + str(player.hands[hand])
        else:
            print player.name + "'s hand " + str(hand)

    def get_bet(self, player):
        print "{0} you currently have {1} points ".format(player.name, player.points)
        return raw_input("{0} please enter your bet (up to {1}) a bet of 0 will remove you from game: ".format(player.name, player.points))

    def show_bet(self, player):
        print "{0} bets {1} out of their {2} points".format(player.name, player.bet, player.points)

    @staticmethod
    def choose():
        # TODO need to capture if another input is entered
        answer = raw_input("\t\t(H)it or (S)tand? : ")
        if answer == 'H' or answer == 'h' or answer == "hit":
            return True
        elif answer == 'S'or answer == 's' or answer == "stand":
            return False

    @staticmethod
    def move(player, move, hand=0):
        if isinstance(hand, (int, long)):
            print player.name + move + "with score of " + str(player.hands[hand].score)
        else:
            print player.name + move + "with score of " + str(hand)

    @staticmethod
    def busted(player, hand=0):
        if isinstance(hand, (int, long)):
            print "BUSTED: " + player.name + "'s hand of " + str(player.hands[hand]) + " :BUSTED"
        else:
            print "BUSTED: " + player.name + "'s hand of  " + str(hand) + " :BUSTED"

    @staticmethod
    def status(player, hand=0):
        if isinstance(hand, (int, long)):
            print player.name + " " + str(player.hands[hand].status) + " with a hand of " + str(player.hands[hand])
        else:
            print player.name + " " + str(player.hands.status) + " with a hand of  " + str(hand)

    @staticmethod
    def show_msg(msg):
        print msg
