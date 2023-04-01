unsorted_list = [101, 49, 3, 12, 56]

def bubblesort(the_list):
  high_idx = len(the_list) - 1
  
  for i in range(high_idx):    #1 value in range denotes stop value. start and step are both assigned default of 1
    for j in range(high_idx):
      item = the_list[j]
      next_item = the_list[j+1]
      
      if item > next_item:
        the_list[j] = next_item
        the_list[j+1] = item
        
      print(the_list, i, j)
    
bubblesort(unsorted_list)