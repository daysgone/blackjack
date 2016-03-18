import random
SUITES = {
        'C': 'Clubs',
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades'
    }
RANKS = {
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        'J': 'jack',
        'Q': 'queen',
        'K': 'king',
        'A': 'ace',
    }


def check_key(key, dict):
    if key in dict:
        return key
    else:
        raise KeyError('please enter a correct suite')


def check_char(full_name, dic):
    for key, value in dic.items():
        if value == full_name:
            return key
    return None


def get_name(char, dic):
    return dic.get(char)


class Card(object):
    def __init__(self, rank, suite):
        # stop everything if not a valid rank or suite
        self._rank = rank
        self._suite = suite
        self.hidden = False

        # special value cases
        if self._rank == 'A':
            self.value = 11
        elif rank in ['K', 'Q', 'J']:
            self.value = 10
        else:
            self.value = rank

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, val):
        self._rank = check_key(val, RANKS)

    def is_ace(self):
        if self.rank == 'A':
            return True
        else:
            False

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, val):
        self._suite = check_key(val, SUITES)

    def hide_card(self):
        self.hidden = True

    def show_card(self):
        self.hidden = False

    def __str__(self):
        if self.hidden:
            return '[X]'
        else:
            return '[' + get_name(self._rank, RANKS) + ' of ' + get_name(self._suite, SUITES) + ']'


class Deck(object):
    """
    collection of cards default deck does not include jokers
    """
    def __init__(self):
        # change deck size by number of suites and ranks in the external files
        self.cards = [Card(rank, suite) for suite in SUITES for rank in RANKS]
        self.shuffle()

    def __str__(self):
        print ','.join(str(p) for p in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def cards(self):
        return self.cards

    def get_card(self):
        # returns last item of list by default
        return self.cards.pop()

    def length(self):
        return len(self.cards)


class Shoe(object):
    """
        Holds multiple Deck objects
    """
    def __init__(self, decks=1):
        self.shoe = [Deck() for _ in xrange(decks)]

    def deal(self):
        # pick a card from a random deck in the shoe
        i = random.randint(0, len(self.shoe)-1)
        print "picked card from deck {0}".format(i+1)
        return self.shoe[i].get_card()


'''test code
shoe = Shoe(2)
new_card = shoe.deal()
print new_card
'''