def linear_search(the_list, target):
  for x in range(len(the_list)):   #note that providing only one value for range uses the value as the stop value
    if the_list[x] == target:
      print('Found at index', x)
      return x
  print('Target is not in the list')
  return -1