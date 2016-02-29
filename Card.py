class EnumException(Exception): pass
class InvalidEnumVal(EnumException): pass
class InvalidEnum(EnumException): pass
class DuplicateEnum(EnumException): pass
class DuplicateEnumVal(EnumException): pass

class enum:
    def __init__(self, enumstr):
        self.lookup = { }
        self.reverseLookup = { }
        evalue = 0

        elist = enumstr.split(',')

        for e in elist:
            item = e.strip().split('=')

            ename = item[0].strip()
            if ename == '':
                continue

            if len(item) == 2:
                try:
                    evalue = int(item[1].strip(), 0)
                except ValueError:
                    raise InvalidEnumVal, 'Invalid value for: ' + ename
            elif len(item) != 1:
                raise InvalidEnum, "Invalid enum: " + e

            if self.lookup.has_key(ename):
                raise DuplicateEnum, "Duplicate enum name: " + ename
            if self.reverseLookup.has_key(evalue):
                raise DuplicateEnumVal,"Duplicate value %d for %s"%(evalue,ename)

            self.lookup[ename] = evalue
            self.reverseLookup[evalue] = ename
            evalue += 1

    def __getattr__(self, attr):
        return self.lookup[attr]

    def __len__(self):
        return len(self.lookup)

    def __repr__(self):
        s = ''
        values = self.lookup.values()
        values.sort()
        for e in values:
            s = s + '%s = %d\n' % (self.reverseLookup[e], e)
        return s
'''
class Card(object):

    Numbers = enum(ONE=1,
               TWO=2,
               THREE=3,
               FOUR=4,
               FIVE=5,
               SIX=6,
               SEVEN=7,
               EIGHT=8,
               NINE=9,
               TEN=10,
               JACK=10,
               QUEEN=10,
               KING=10,
               ACE=1
               )

    Suit = enum(CLUBS = 'C',
                DIAMONDS = 'D',
                HEARTS = 'H',
                SPADES = 'S'
                )
    def __init__(self,suit,rank):
        self.suit = self.Suit.CLUBS
        self.rank = rank

        #assign point value to card depending on what card
        # Ace can either be 1 or 11
        self.hidden = False

    def hideCard(self):
        self.hidden = True

    def showCard(self):
        self.hidden = False
'''
str="""ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN"""
v=enum(str)
print v
print 'ONE = %d' % v.ONE