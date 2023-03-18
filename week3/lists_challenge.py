import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
  draw_card = input('Press Enter to pick a card. \nPress "Q" followed by enter to quit.\n')
  if draw_card.lower() == 'q':
    print('\nYou have quit. \nGoodbye!\n\n')
    break
  else:
    random_card = random.choice(diamonds)
    diamonds.remove(random_card)
    hand.append(random_card)
    
    print('Your hand:', hand)
    print('Remaining cards:', diamonds)
    
if not diamonds:
  print('There are no more cards to pick.')