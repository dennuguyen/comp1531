# COMP1531 Lab 02
#
# Dan Nguyen (z5206032)
# 25/2/2020

def check_password(password):

    # set flags for password parsing
    number = False
    upper = False
    lower = False

    for letter in password:
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True
        elif letter.isdigit():
            number = True

    # if-else conditions for password strength
    if len(password) >= 12 and upper and lower and number:
        return 'Strong Password'
    elif len(password) >= 8 and number:
        return 'Moderate Password'
    elif password == 'password' or password == 'iloveyou' or password == '123456':
        return 'Horrible Password'
    else:
        return 'Poor Password'

def test_password():
    assert check_password('ihearttrimesters') == 'Poor Password'
    assert check_password('ihatetrimesters1111') == 'Moderate Password'
    assert check_password('iHATEtrimesters1111') == 'Strong Password'
    assert check_password('password') == 'Horrible Password'
    assert check_password('') == 'Poor Password'

if __name__ == '__main__':
    test_password()
