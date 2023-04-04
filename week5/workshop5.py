import random

def guess_random_number(tries, start, stop):
  random_number = random.randrange(start, stop + 1)
  
  while tries != 0:
    print('Attempts remaining:', tries)
    
    user_guess = int(input(f'Guess a number between {start} and {stop}: '))
    
    if user_guess == random_number:
      print('You successfully guessed the magic number!')
      
    elif user_guess > random_number:
      print('Guess lower!')
      tries -= 1
      
    elif user_guess < random_number:
      print('Guess higher!')
      tries -= 1
      
  print('Sorry! You ran out of tries before you guessed the magic number.')
  
guess_random_number(3, 1, 10)