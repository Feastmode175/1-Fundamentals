class User:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
    
  def change_password(self, password):
    self.password = password
    print('Your password has been changed to', password)

#syntax for sub class is class SubClass(SuperClass)    
class BankUser(User):
  def __init__(self, name, email, password):
    #remember that an init func in a subclass removes superclass func
    super().__init__(name, email, password)
    self.balance = 0 
    
  def check_balance(self):
    print(self.name, 'has an account balance of:', self.balance)
    

bankuser1 = BankUser('Jane', 'jane@nucamp.co', 'best password')