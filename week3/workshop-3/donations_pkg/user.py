def login(database, username, password):
  if username in database and database[username] == password:
    print ('Welcome', username + '!')
    return username
  elif username in database and database[username] != password:
    print('Incorrect password for', username, '\n')
    return ''
  else:
    print('Username not found. Please register. \n')
    return ''
  
  
def register(database, username):
  if username in database:
    print('Username already registered. \n')
    return ''
  else:
    print(username, 'has been registered.')
    return username
  
def donate(username):
  donation_amount = input('Enter an amount to donate: ')
  donation_string = username + ' donated ' + donation_amount
  print('Thank you for your donation', username + '!')
  return donation_string

def show_donations(donations):
  print('\n---All Donations---')
  if donations == []:
    print('There are no donations.')
  else:
    for donation in donations:
      print(donation)