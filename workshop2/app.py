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
print('=== Automated Teller Machine ===')
name = input('Enter Name to register: ')
pin = input('Enter PIN: ')
current_balance = 0

#display user's current name and balance
print(name, 'has been registered with a starting balance of $' + str(current_balance), '\n')

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
        

while True:                         #assign options menu
    atm_menu(name)
    option = input('Choose an option: ')
    
    if option == '1':
        show_balance(current_balance)
    elif option == '2':
        current_balance = deposit(current_balance)
        print('Current balance is now:', current_balance)
    elif option == '3':
        current_balance = withdraw(current_balance)
        print('Current balance is now:', current_balance)
    elif option == '4':
        logout(name)
        break