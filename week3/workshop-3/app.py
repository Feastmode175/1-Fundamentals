from donations_pkg.homepage import show_homepage
from donations_pkg.user import *

database = {
  'admin': 'password123'
}

donations = []

authorized_user = ''

while True:
  show_homepage()

  # ensure user is logged in and display user name
  if authorized_user == '':
    print('You must be logged in to donate.')
  else:
    print('You are logged in as: ', authorized_user)

  option = input('\nPlease choose an option. ')

  #define user options
  #option 1: make sure user is logged in correctly
  if option == '1':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    authorized_user = login(database, username, password)
  
  # option 2: make sure user is new and add new username/pw to database
  elif option == '2':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    user_to_register = register(database, username)
    if user_to_register != '':  #I chose not to use 'authorized_user' to stop the require the user to log in manually after registering
      database[user_to_register] = password
  
  #option 3: make sure user is logged in, allow user to make donation, add to donations list
  elif option == '3':
    if authorized_user == '':
      print('You must be logged in to donate.')
    else:
      donation_string = donate(authorized_user)
      donations.append(donation_string)
      print(donations)
  elif option == '4':
    print('Test 4')
    show_donations()
  elif option == '5':
    print('Goodbye!')
    break