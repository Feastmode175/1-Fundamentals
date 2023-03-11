import random

high_score = 0

def dice_game():
  global high_score
  while True:
    print('Current High Score: ', high_score)
    print('1) Roll Dice \n2) Leave Game')
    roll_dice = input('Enter your choice: ')
    
    if roll_dice == '1' or roll_dice.lower() == 'roll dice':
      dice_1 = random.randint(1, 6)
      print('You roll a...',dice_1)
      
      dice_2 = random.randint(1, 6)
      print('You roll a...',dice_2)
      
      total = dice_1 + dice_2
      print('You have rolled a total of: ', total, '\n')
      
      if (total > high_score):
        high_score = total
        print('New high score!! \n')
    if roll_dice == '2' or roll_dice.lower() == 'leave game':
      print('Goodbye!')
      break
    
    
dice_game()
