# COMP1531 Tutorial 02
#
# Dan Nguyen (z5206032)
# 24/2/2020

# Compute the average of only the positive elements in the list.
def rainfall(integers):

    positive_integers = [i for i in integers if i > 0]

    if len(positive_integers) == 0:
        return 0

    return sum(positive_integers) / len(positive_integers)

# Write tests here
def test_rainfall():
    assert rainfall( [1, 2, 3, 4, 5, 6] ) == 3.5
    assert rainfall( [0, -2, -4] ) == 0
    assert rainfall( [1, 28, -1] ) == 14.5
    assert rainfall( [] ) == 0
    assert rainfall ([0.4, 1.5, -6.2, 1.0] ) == 29 / 30

    print('All tests passed!')

test_rainfall()