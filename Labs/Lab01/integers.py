# COMP1531 Lab 01
#
# Dan Nguyen (z5206032)
# 17/2/2020

integers = [1, 2, 3, 4, 5]

integers.append(6)

answer = 0

for number in integers:
    answer += number

print(answer)

print(sum(integers)) # short-cut