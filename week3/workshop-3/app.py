from donations_pkg.homepage import show_homepage

database = {
  'admin': 'password123'
}

donations = []

authorized_user = ''

show_homepage()

# ensure user is logged in and display user name
if authorized_user == '':
  print('You must be logged in to donate.')
else:
  print('You are logged in as: ', authorized_user)

option = input('Please choose an option.')

#define user options

if option == '1':
  print('Test 1')
  #TODO write login functionality
elif option == '2':
  print('Test 2')
  #TODO: write register functionality
elif option == '3':
  print('Test 3')
  #TODO: write donate functionality
elif option == '4':
  print('Test 4')
  #TODO: write show donations functionality
elif option == '5':
  print('Test 5')
  print('Goodbye', authorized_user)
