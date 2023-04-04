import random

def guess_random_number(tries, start, stop):
  #generate random number
  random_number = random.randrange(start, stop + 1)
  
  # set number of attempts
  while tries != 0:
    print('Attempts remaining:', tries)
    
    #have user guess
    user_guess = int(input(f'Guess a number between {start} and {stop}: '))
    
    #display correct message based on user input
    if user_guess == random_number:
      print('You successfully guessed the magic number!')
      
    elif user_guess > random_number:
      print('Guess lower!')
      tries -= 1
      
    elif user_guess < random_number:
      print('Guess higher!')
      tries -= 1
      
  print(f'Sorry! You ran out of tries before you guessed the magic number: {random_number}')
  
#guess_random_number(5, 0, 10)


def guess_number_linear(tries, start, stop):
  # generate random number
  random_number = random.randrange(start, stop + 1)
  
  #set number of attempts
  while tries != 0:
    print(f'The program will have {tries} attempts to guess the number.\n')
    #attempt to find number using linear search
    for i in range(start, stop + 1):
      print(f'The program has guessed: {i}')
      
      #display appropriate feedback
      if i == random_number:
        print('The program has found the correct number.')
        return i
        
      else:
        tries -= 1
        print('Attempts remaining:', tries)
      
      #i couldn't figure out why the loop would break when tries dropped to 0 so i added this line
      if tries == 0:
        break
    
  print('The program has failed to guess the correct number:', random_number)
      

guess_number_linear(5, 0, 10)