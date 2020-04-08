'''
Tocaciu Valeria - UMT Internship
'''
def passwordChecker(password):
    changes = {'addChr': 0, 'removeChr': 0, 'types': 0, 'repeatingChr': 0}
    if len(password) < 6:
        changes['addChr'] = 6 - len(password)
    elif len(password) > 20:
        changes['removeChr'] = len(password) - 20
    lowercase = False
    uppercase = False
    digit = False
    for letter in password:
        if letter.isupper():
            uppercase = True
        if letter.islower():
            lowercase = True
        if letter.isdigit():
            digit = True
    if not lowercase:
        changes['types'] = changes['types'] + 1
    if not uppercase:
        changes['types'] = changes['types'] + 1
    if not digit:
        changes['types'] = changes['types'] + 1
    if changes['addChr'] != 0:
        return firstCase(password, changes)
    if changes['addChr'] == 0 and changes['removeChr'] == 0:
        return secondCase(password, changes)
    if changes['removeChr'] != 0:
        return thirdCase(password, changes)
    return 0


def firstCase(password, changes):
    if changes['addChr'] >= changes['types']:
        changes['types'] = 0
    i = 0
    while i < len(password) - 2:
        if password[i] == password[i + 1] == password[i + 2]:
            if changes['addChr'] != 0:
                changes['addChr'] = changes['addChr'] - 1
            if changes['types'] != 0:
                changes['types'] = changes['types'] - 1
            changes['repeatingChr'] = changes['repeatingChr'] + 1
            i = i + 2
        i = i + 1
    return sum(list(changes.values()))


def secondCase(password, changes):
    i = 0
    while i < len(password) - 2:
        if password[i] == password[i + 1] == password[i + 2]:
            if changes['types'] != 0:
                changes['types'] = changes['types'] - 1
            changes['repeatingChr'] = changes['repeatingChr'] + 1
            i = i + 2
        i = i + 1
    return sum(list(changes.values()))


def thirdCase(password, changes):
    i = 0
    while i < len(password) - 2:
        if password[i] == password[i + 1] == password[i + 2]:
            if changes['types'] != 0 and changes['removeChr'] == 0:
                changes['types'] = changes['types'] - 1
            if changes['removeChr'] != 0:
                changes['removeChr'] = changes['removeChr'] - 1
            if changes['removeChr'] == 0:
                i = i + 2

            changes['repeatingChr'] = changes['repeatingChr'] + 1
        i = i + 1
    return sum(list(changes.values()))


def tests():
    assert (passwordChecker("") == 6)
    assert (passwordChecker("a") == 5)
    assert (passwordChecker("aaaa") == 2)
    assert (passwordChecker("111456") == 2)
    assert (passwordChecker("aaaaaaaaaaaaaaaaaaaaa") == 7)  # remove one 'a' character and replacing 6 a's with
    # another one while making sure one is a digit and another one uppercase =  min 7 changes


if __name__ == '__main__':
    tests()
    passw = input("Password: ")
    print("Number of changes:", passwordChecker(passw))
