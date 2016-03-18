import os
from Game import Game

#os.system('cls') # windows


def clear():
    os.system('clear')# linux/osx

clear()
prompt = int(raw_input("How many players? : "))
clear()

names = []
for n in xrange(1, prompt+1):
    names.append(raw_input("Please enter Player{0}'s name? : ".format(n)))
    clear()

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
                print p.name + " BUSTED with a score of {0}\n".format(hand.score)
        elif answer == 'S'or answer == 's' or answer == "stand":
            keep_going = False
            print p.name + ": stands with a hand of " + str(p.hand[0]) + "\n"


# TODO this probably should be in controller
# dealer hits if score is less then 16
if dealer.hand[0].score <= 16:
    bust, hand = blackjack.hit(dealer)
    print "Dealer hits:"
    print hand
    if bust:
        # TODO only name the people who didnt bust
        print "dealer busted with a score of {0}".format(hand.score)
        for p in players:
            names = ''
            # TODO bust happens per hand
            if not p.hand[0].is_bust:
                names += p.name + ', '
            names += 'wins'
        print names


# if dealer under 21 pay players with a higher score
# take money from those with lower
# tie with player, refund bet

# start new hand

# show cards in players hand
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