import Suites
import Ranks


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
        self._rank = Ranks.check(val)

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
        self._suite = Suites.check(val)

    def hide_card(self):
        self.hidden = True

    def show_card(self):
        self.hidden = False

    # TODO
    # ace special case

    def __str__(self):
        if self.hidden:
            return '[X]'
        else:
            return '[' + Ranks.rank_name(self._rank) + ' of ' + Suites.suite_name(self._suite) + ']'

''' Tester code
test = Card('K', 'H')
print test
print test.value
print test.rank
print test.is_ace()
print Suites.suite_name(test.suite)
'''