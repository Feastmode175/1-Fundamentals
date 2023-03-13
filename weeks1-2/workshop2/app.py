from banking_pkg.account import *

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
while True:
    print('=== Automated Teller Machine ===')
    
    #ensure user name is a max of 10 char
    while True:
        name = input('Enter Name to register: ')
        if len(name) > 10:
            print('The maximum name length is 10 characters. \n')
        else:
            break
    
    #ensure user pin is 4 digits
    while True:
        print('=== Automated Teller Machine ===')
        pin = input('Enter PIN: ')
        if pin.isnumeric() == False or len(pin) != 4:
            print('Pin must be 4 numbers. \n')
        else:
            break
    
    #double check that user is satisfied with credentials
    print('\n\nYour current username is:', name)
    print('Your current PIN is: ', pin)
    verify_user_info = input('Is this correct? \nYes or No? ')
    if verify_user_info.lower() == 'no':
        continue
    elif verify_user_info.lower() == 'yes':         
        #display user's current name and balance
        current_balance = 0
        print(name, 'has been registered with a starting balance of $' + str(current_balance), '\n')
        break
    else:
        print('Invalid choice. Please reenter your username and PIN \n')
    

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
        

#assign options
while True:                         
    atm_menu(name)
    option = input('Choose an option: ')
    
    if option == '1':
        show_balance(current_balance)
    elif option == '2':
        current_balance = deposit(current_balance)
        print('Current balance is now:', current_balance)
    elif option == '3':
        current_balance = withdraw(current_balance, name)
        print('Current balance is now:', current_balance)
    elif option == '4':
        logout(name)
        break