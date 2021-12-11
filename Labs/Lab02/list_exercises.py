# COMP1531 Lab 02
# This exercise assumes integer operations only
#
# Dan Nguyen (z5206032)
# 24/2/2020

def reverse_list(integers):

    integers.reverse() # does not return a value

    # return integers[::-1] # if re-assigning value

def minimum(integers):

    # removes alpha
    integers = [i for i in integers if isinstance(i, int)]

    # if list is empty
    if len(integers) == 0:
        return None

    # integers.sort() # does not return a value
    return sorted(integers)[0] # single-line

def sum_list(integers):

    # removes alpha
    integers = [i for i in integers if isinstance(i, int)]

    # if list is empty
    if len(integers) == 0:
        return None

    return sum(integers) # single-line
