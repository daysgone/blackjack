# MODEL
ranks = {
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

''' bother with ASCII and lower case?
        'j': 'jack',
        'q': 'queen',
        'k': 'king',
        'a': 'ace',
        65: 'ace',
        97: 'ace',
        74: 'jack',
        106: 'jack',
        75: 'king',
        107: 'king',
        81: 'queen',
        113: 'queen'
    }
'''


def check(key):
    if key in ranks:
        return key
    else:
        print "key error"
        return None
        #raise KeyError('please enter a correct rank')


def rank_name(key):
    # .get returns None if key not found in dict
    return ranks.get(key)


def rank_char(full_name):
    for key, value in ranks.items():
        if value == full_name:
            return key
    return 'None'

#test code

#print rank_name('B')
#print rank_char('three')
#print check(1)
#print check(12)
