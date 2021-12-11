# COMP1531 Lab 01
#
# Dan Nguyen (z5206032)
# 17/2/2020

strings = ['This', 'list', 'is', 'now', 'all', 'together']

sentence = ''

for word in strings:
    sentence += word + ' '

# sentence = sentence[:-1]
sentence.strip() # removes leading and trailing whitespace

print(sentence)

print(' '.join(strings)) # short-cut