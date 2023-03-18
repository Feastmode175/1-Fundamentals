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
    print('Username already registered \n')
    return ''
  else:
    print(username, 'has been registered.')
    return username