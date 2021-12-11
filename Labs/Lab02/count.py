# COMP1531 Lab 02
#
# Dan Nguyen (z5206032)
# 25/2/2020

def count_char(input):
    
    dictionary = {}

    for i in input:
        if i in dictionary.keys(): # if key exists
            dictionary[i] += 1

        else: # key does not exist yet
            dictionary[i] = 1

    return dictionary
