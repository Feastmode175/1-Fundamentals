states = ['Washington', 'Oregon', 'California']

#iterates through list and prints each value
'''
for state in states:
  state = state.lower()
  print(state)
'''
  
#"_______ in states" will evaluate to a boolean
'''
print('Washington' in states)
print('Tennessee' in states)
print('Washington' not in states)
'''

#lists can be concatenated
states2 = ['Arizona', 'Ohio', 'Louisiana']
best_states = states + states2
print(best_states)

#slicing grabs items from lists
#lists[start:end] ending index is EXCLUSIVE!!
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])