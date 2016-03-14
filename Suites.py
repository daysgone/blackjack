# MODEL
suites = {
        'C': 'Clubs',
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades'
    }


def check(key):
    if key in suites:
        return key
    else:
        raise KeyError('please enter a correct suite')


def suite_name(char):
    return suites.get(char)


def suite_char(fullName):
    for key, value in suites.items():
        if value == fullName:
            return key
    return None


'''
print suite_name('C')
print suite_char('Clubs')
'''