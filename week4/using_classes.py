class Player:
  max_hp = 4000


#instantiate an object from a class
player1 = Player()
print(player1.max_hp) #access attribute of player class
player2 = Player()
print(player2.max_hp)

#value of class attribute changed (affects all associated objects)
Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp)