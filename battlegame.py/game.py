wizard = 'Wizard'
elf = 'Elf'
human = 'Human'

wizard_hp = 70
wizard_damage = 150

elf_hp = 100
elf_damage = 100

human_hp = 150
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
  print('1) Wizard \n2) Elf \n3) Human')
  character = input('Choose your character: ')
  
  if character == "1":
    my_character = wizard
    my_hp = wizard_hp
    my_damage = wizard_damage
    break
  elif character == "2":
    my_character = elf
    my_hp = elf_hp
    my_damage = elf_damage
    break
  elif character == "3":
    my_character = human
    my_hp = human_hp
    my_damage = human_damage
    break
  else:
    print('Unknown Character')
    
print('You have chosen the character:', my_character,)
print('Health:', my_hp)
print('Damage:', my_damage)

while True:
  dragon_hp -= my_damage
  print('The', my_character, 'attacked the Dragon!')
  print('The', my_character, 'has', my_hp, 'remaining.')
  if dragon_hp <= 0:
    print('The Dragon has lost the battle!')
    break
  my_hp -= dragon_damage
  print('The dragon has attacked the', my_character)
  print('The', my_character, 'has', my_hp, 'health remaining.')
  if my_hp <= 0:
    print('The', my_character, 'has lost the battle!')
