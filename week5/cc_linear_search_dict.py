def linear_search_dictionary(dictionary, target):
  for key, value in dictionary.items():
    if value == target:
      print(f'found at key {key}')
      return key
    
  print(f'{target} is not in the list.')
  return None
  

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)