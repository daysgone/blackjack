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
        for n in xrange(1, prompt+1):
            self.players.extend(raw_input("Please enter Player{0}'s name? : ".format(n)))
            self.clear()
        return self.players

    @staticmethod
    def deal():
        # TODO do somethign better here
        answer = raw_input("Ready to Deal?")
        #if answer:
        return True

    @staticmethod
    def update_hand(player, hand=0):
        if isinstance(hand, (int, long)):
            print player.name + "'s hand now is " + str(player.hand[hand])
        else:
            print player.name + "'s hand now is " + str(hand)

    @staticmethod
    def choose():
        answer = raw_input("\t(H)it or (S)tand? : ")
        if answer == 'H' or answer == 'h' or answer == "hit":
            return True
        elif answer == 'S'or answer == 's' or answer == "stand":
            return False

    @staticmethod
    def hit(player, hand=0):
        if isinstance(hand, (int, long)):
            print player.name + " hits on the hand of " + str(player.hand[hand])
        else:
            print player.name + " hits on the hand of " + str(hand)

    @staticmethod
    def stand(player, hand=0):
        if isinstance(hand, (int, long)):
            print player.name + " stands on the hand of " + str(player.hand[hand])
        else:
            print player.name + " stands on the hand of " + str(hand)

    @staticmethod
    def busted(player, hand=0):
        if isinstance(hand, (int, long)):
            print "BUSTED: " + player.name + "'s hand of " + str(player.hand[hand]) + " :BUSTED"
        else:
            print "BUSTED: " + player.name + "'s hand of  " + str(hand) + " :BUSTED"

    @staticmethod
    def winner(player, hand=0):
        if isinstance(hand, (int, long)):
            print "WINNER: " + player.name + " with a hand of " + str(player.hand[hand]) + " :WINNER"
        else:
            print "WINNER: " + player.name + "'s hand of  " + str(hand) + " :WINNER"



'''
# start up game
blackjack = Game(names)
dealer = blackjack.dealer
players = blackjack.players

# place bets
for p in players:
    blackjack.place_bets()
    pass

# deal cards
print "Dealer deals cards"
blackjack.deal_cards()

#show current hands
for p in players:
    print p.name + " currently has " + str(p.hand[0])

print "Dealer currently has " + str(dealer.hand[0])

# if dealers first card is an Ace
    # ask players if they want insurance
        # half of orig bet

clear()
# dealer flip over 2nd card
blackjack.show_card(dealer)
print "Dealer flips 2nd card to show " + str(dealer.hand[0]) + "\n"
# if blackjack take orig bets from those who did not buy insurance
# if insurance not bought only players with blackjack keep orig bet

busted = 0
# start with first player, hit until bust or stand, continue with other players
for p in players:
    keep_going = True

    while keep_going:
        print p.name + " currently has a score of " + str(p.hand[0].score)
        answer = raw_input("\t(H)it or (S)tand? : ")

        if answer == 'H' or answer == 'h' or answer == "hit":
            print p.name + ": hits"
            bust, hand = blackjack.hit(p)
            print hand
            if bust:
                # returns true if the score is now over 21
                keep_going = False
                bust += 1
                print p.name + " BUSTED with a score of {0}\n".format(hand.score)
        elif answer == 'S'or answer == 's' or answer == "stand":
            keep_going = False
            print p.name + ": stands with a hand of " + str(p.hand[0]) + "\n"


# if both players bust then no need to have dealer hit
if busted != len(players):
    # dealer hits if score is less then 16
    bust, hand = blackjack.hit(dealer)
    if bust:
        # TODO only name the people who didnt bust
        print "dealer busted on hand {0} with a score of {1}".format(hand, hand.score)
        for p in players:
            names = ''
            # TODO bust happens per hand
            if not p.hand[0].is_bust:
                names += p.name + ', '
            names += 'wins'
        print names
else:
    print "Dealer wins!!!"

# if dealer under 21 pay players with a higher score
# take money from those with lower
# tie with player, refund bet

# start new hand

# show cards in players hand
'''
'''
for p in players:
    print p.name + 's hand ' + str(p.hand[0])

print dealer.name + 's hand ' + str(dealer.hand[0])

for p in players:
    print
    if blackjack.hit(p, 0):
        print p.hand[0]
    else:
        print p.name + ' busted'
#blackjack.stand(players[0], players[0].hand[0])
#print blackjack.dealer.name
print blackjack.hit(dealer, 0)
print dealer.hand[0]

'''