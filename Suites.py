# MODEL
SUITES = {
        'C': 'Clubs',
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades'
    }


def check(key):
    if key in SUITES:
        return key
    else:
        raise KeyError('please enter a correct suite')


def suite_name(char):
    return SUITES.get(char)


def suite_char(fullName):
    for key, value in SUITES.items():
        if value == fullName:
            return key
    return None


'''
print suite_name('C')
print suite_char('Clubs')
'''