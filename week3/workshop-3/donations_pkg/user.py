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
  
  if donation_amount.isdigit() == False or float(donation_amount) <= 0:
    print('Donation must be an amount that is greater than $0.')
  else: 
    donation_string = username + ' donated ' + donation_amount
    print('Thank you for your donation', username + '!')
    return donation_string

def show_donations(donations, username):
  print('\n---All Donations---')
  if donations == []:
    print('There are no donations.')
  else:
    #admin will show all donations
    if username == 'admin':
      for donation in donations:
        print(donation)
    else:
      #limit user to only seeing their donations
      for donation in donations:
        if donation[0:len(username)] == username:
          print(donation)