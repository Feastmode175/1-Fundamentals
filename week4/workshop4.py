#make a class user with name, pin and password
class User:
  def __init__(self, name, pin, password):
    self.name = name
    self.pin = pin
    self.password = password
  
  #update name
  def change_name(self, new_name):
    self.name = new_name
  
  #update pin
  def change_pin(self, new_pin):
    self.pin = new_pin
  
  #update password
  def change_password(self, new_password):
    self.password = new_password


class BankUser(User):
  def __init__(self, name, pin, password,):
    super().__init__(name, pin, password)
    self.balance = 0








""" Driver Code for Task 1 """
#instantiate test_user and show attributes
test_user = User('Bob', 1234, 'password')
""" print(test_user.name)
print(test_user.pin)
print(test_user.password) """

""" Driver Code for Task 2 """
#change test user attributes and display
""" test_user.change_name('Bobby')
test_user.change_pin('4321')
test_user.change_password('newpassword') """
""" 
print(test_user.name)
print(test_user.pin)
print(test_user.password) """

""" Driver Code for Task 3 """
# instantiate test bank user and test functionality
test_bank_user = BankUser('Chuck', 5678, 'password123')
print(test_bank_user.name)
print(test_bank_user.pin)
print(test_bank_user.password)
print(test_bank_user.balance)

test_bank_user.change_name('Chucky')
test_user.change_pin('8765')
test_user.change_password('password456')

print(test_bank_user.name)
print(test_bank_user.pin)
print(test_bank_user.password)
print(test_bank_user.balance)