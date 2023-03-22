class User:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
    
  def change_password(self, password):
    self.password = password
    print('Your password has been changed to', password)
    
user1 = User('Jane', 'jane@nucamp.co', 'janespassword') 
print(user1.password)

#instance method can be used to change password
user1.change_password('bestpassword')