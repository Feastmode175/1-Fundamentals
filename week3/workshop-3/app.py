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
    authorized_user = register(database, username)
    if username != '':
      database[authorized_user] = password
      
  elif option == '3':
    print('Test 3')
    #TODO: write donate functionality
  elif option == '4':
    print('Test 4')
    #TODO: write show donations functionality
  elif option == '5':
    print('Goodbye', authorized_user +'!')
    break