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
print(name, 'has been registered with a starting balance of $' + str(balance))