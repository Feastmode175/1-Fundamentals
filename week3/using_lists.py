states = ['Washington', 'Oregon', 'California']

#bracket notation can be used to access items in list
'''
print(states[0])
print(states[1])
print(states[2])
'''

#using a negative number for index will start from the end (-1 is the last item)
'''
print(states[-1])
print(states[-2])
print(states[-3])
'''

#lists are mutable meaning they can be altered
states[2] = 'Arizona'
'''
print(states)
'''

#len returns the length of a list
'''
print(len(states))
'''

#methods are functions that act on "objects" such as lists
#append adds item to end of list
states.append('New York')
print(states)

#pop will remove the last item in a list unless an index is provided
states.pop()
print(states)
states.pop(1)
print(states)