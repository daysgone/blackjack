DEBUG = False

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


def check_key(key, dic):
    if key in dic:
        return key
    else:
        raise KeyError('please enter a correct value')


def check_char(full_name, dic):
    for key, value in dic.items():
        if value == full_name:
            return key
    return None


def get_name(char, dic):
    return dic.get(char)


class Card(object):
    def __init__(self, rank, suite, vis=False):
        """ initialization of card
        :param rank: see key values from RANKS
        :param suite: see key values from SUITES
        :param vis: False would be face down
        """
        # stop everything if not a valid rank or suite
        self.rank = rank
        self.suite = suite
        self.visibility = vis
        self.is_ace = False

        # special value cases
        if self.rank == 'A':
            self.is_ace = True
            self.value = 11
        elif rank in ['J', 'Q', 'K']:
            self.value = 10
        else:
            self.value = rank

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, val):
        self._rank = check_key(val, RANKS)

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, val):
        self._suite = check_key(val, SUITES)
    '''
    @property
    def visibility(self):
        return self._visibility

    @visibility.setter
    def visibility(self, val):
        self._visibility = val
    '''
    @property
    def is_ace(self):
        return self._is_ace

    @is_ace.setter
    def is_ace(self, val):
        self._is_ace = val

    def __str__(self):
        if self.visibility:
            return '[' + get_name(self._rank, RANKS) + ' of ' + get_name(self._suite, SUITES) + ']'
        else:
            return '[X]'

if DEBUG:
    ''' Tester code'''
    print "-----Begin Card Module test--------"
    test = Card('A', 'H', False)
    print test
    print test.value
    print test.rank
    print "hidden? %s" % test.is_ace
    print get_name(test.suite, SUITES)

    print "-----End Card Module code--------- "
