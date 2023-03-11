def show_balance(balance):
  print('Current balance: ', balance)
  
def deposit(balance):
  deposit_amount = input('Enter amount to deposit: ')
  return balance + float(deposit_amount)

def withdraw(balance):
  withdrawal_amount = input('Enter amount to withdraw: ')
  return balance - float(withdrawal_amount)

def logout(name):
  print('Goodbye', name)