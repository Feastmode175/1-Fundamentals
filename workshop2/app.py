def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#collect user's name, pin, and current balance
print('=== Automated Teller Machine ===')
name = input('Enter Name to register: ')
pin = input('Enter PIN: ')
balance = 0

#display user's current name and balance
print(name, 'has been registered with a starting balance of $' + str(balance), '\n')

#login validation
while True:
    print('LOGIN')                                              
    name_to_validate = input('Enter Name: ')
    pin_to_validate = input('Enter PIN: ')          
    
    if name_to_validate == name and pin_to_validate == pin:    
        print('Login Successful \n')
        break
    else:
        print('Invalid Credentials! \n')
        
#
while True:
    atm_menu(name)
    option = input('Choose an option: ')