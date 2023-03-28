








""" Driver Code for Task 1 """
class User:
  def __init__(self, name, pin, password):
    self.name = name
    self.pin = pin
    self.password = password
    
test_user = User('Bob', 1234, 'password')
print(test_user.name)
print(test_user.pin)
print(test_user.password)