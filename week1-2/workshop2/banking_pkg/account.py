def show_balance(balance):
  print('Current balance: ', balance)
  
def deposit(balance):
  deposit_amount = input('Enter amount to deposit: ')
  print('You have deposited:', deposit_amount)
  return balance + float(deposit_amount)

def withdraw(balance, name):
  withdrawal_amount = input('Enter amount to withdraw: ')
  
  #below is the logic to make sure balance does not go negative upon withdrawal
  if balance - float(withdrawal_amount) < 0:
    print("Now you KNOW that you don't have that much money. Try again", name)
    return balance
  else:
    print('You have withdrawn:', withdrawal_amount)
    return balance - float(withdrawal_amount)

def logout(name):
  print('Goodbye', name + '!')
  