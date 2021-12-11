president = {
    'name' : 'Ian Jacobs',
    'age' : 54,
    'staff' : [ 'Sally', 'Bob', 'Rob', 'Hayden' ]
}

# Removing Hayden cause we don't like him
president['staff'].remove('Hayden')

# Sorting staff list in alpha
president['staff'].sort()

# Add marks key
president['marks'] = {'20T1': 77, '20T2': 88, '20T3': 99}

if __name__ == '__main__':
	print(president)
