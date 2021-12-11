# COMP1531 Lab 02
#
# Dan Nguyen (z5206032)
# 25/2/2020

def income_tax(income):

    income = float(income) # convert from str to float

    if income < 18201:
        return 0
    elif 18201 <= income and income < 37001:
        return income * 0.19
    elif 37001 <= income and income < 87001:
        return income * 0.325
    elif 87001 <= income and income < 180001:
        return income * 0.37
    else: # income > 180001
        return income * 0.45
    

def io_tax():
    income = input('Enter your income: ')
    print('The estimated tax on your income is $%.2f\n' % income_tax(income))

while 1:
    io_tax()