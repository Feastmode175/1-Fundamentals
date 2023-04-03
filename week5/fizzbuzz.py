def fizzbuzz(upper_bound):
  for i in range(1, upper_bound + 1):
    
    if (i % 3 == 0) and (i % 5 == 0):
      print('FizzBuzz')
    elif i % 3 == 0:
      print('Fizz')
    elif i % 5 == 0:
      print('Buzz')
    else:
      print(i)

fizzbuzz(50)