import random

pips = random.randint(1, 6)
print('You roll the die... it lands with', pips, 'pips showing.')


prizes = ['a car', '$10000', 'a pony', '$500000']
prize_won = random.choice(prizes)
print('You turn the wheel of fortune... It lands on a prize of', prize_won, '!!')