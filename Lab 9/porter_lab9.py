# Alec Porter Lab 9


# Classes --------------------------------------------------------------------------------

class Bank:
    def __init__(self):
        self.__accounts = dict()

    def add_account(self, account):
        self.__accounts[account.get_account_number()] = account

    def get_account(self, account_number):
        return self.__accounts[account_number]

    def list_accounts(self):
        print('\nList of Accounts')
        for number, details in self.__accounts.items():
            print(f'Account Number: {number}, Holder Name: {details.get_holder_name()}')

    def display_account_info(self, account_number):
        account_info = self.__accounts[account_number]
        account_info.display_account_info()
        

class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def display_account_info(self):
        print(f'Account Balance for {self.__holder_name}: ${self.__balance}')


# Functions -----------------------------------------------------------------------------

# check for valid menu option
def menu_check():
    isValid = False
    while not isValid:
        selection = str(input('Enter Your Choice: '))
        if selection != '1' and selection != '2' and selection != '3' and selection != '4' and selection != '5':
            print('You did not enter a valid option, try again.')
            isValid = False
        else:
            isValid = True
    return selection

# check for valid withdraw value
def value_check_withdraw():
    isValid = False
    while not isValid:
        try:
            amount = float(input('Enter Withdraw Amount: ' ))
            while amount <= 0:
                print('That was not a positive value, try again.')
                amount = float(input('Enter Withdraw Amount: '))     
            isValid = True
        except ValueError:
            print('That was not a valid number, try again.')
            isValid = False
    return amount

# check for valid deposit value
def value_check_deposit():
    isValid = False
    while not isValid:
        try:
            amount = float(input('Enter Deposit Amount: ' ))
            while amount <= 0:
                print('That was not a positive value, try again.')
                amount = float(input('Enter Deposit Amount: '))     
            isValid = True
        except ValueError:
            print('That was not a valid number, try again.')
            isValid = False
    return amount

# check for valid accout number
def acct_check():
    isValid = False
    while not isValid:
        try:
            selection = str(input('Enter Your Account Number: '))
            bank.get_account(selection)
            isValid = True
        except KeyError:
            print('That was not a valid account number, try again.')
            isValid = False
    return selection



# Initialize accounts -------------------------------------------------------------------
bankaccount1 = BankAccount('001','Alec',2500.25)
bankaccount2 = BankAccount('002','Bob',500.00)
bankaccount3 = BankAccount('003','Sue',15500.75)

bank = Bank()
bank.add_account(bankaccount1)
bank.add_account(bankaccount2)
bank.add_account(bankaccount3)


# Main Program --------------------------------------------------------------------------

def main():

    '''# Initialize accounts
    bankaccount1 = BankAccount('001','Alec',2500.25)
    bankaccount2 = BankAccount('002','Bob',500.00)
    bankaccount3 = BankAccount('003','Sue',15500.75)

    bank = Bank()
    bank.add_account(bankaccount1)
    bank.add_account(bankaccount2)
    bank.add_account(bankaccount3)'''

    # initialize menu
    menuOption = ''

    while menuOption != '5':
        print('\nBank Menu')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        print('4. List Accounts')
        print('5. Exit')
        menuOption = menu_check()

        if menuOption == '4':
            bank.list_accounts()

        elif menuOption == '3':
            selection = acct_check()
            bank.display_account_info(selection)  # display account information

        elif menuOption == '2':
            selection = acct_check()
            account_data = bank.get_account(selection)
            withdraw = value_check_withdraw()  
            account_data.withdraw(withdraw)     # update account with withdraw
            print(f'Withdrew ${withdraw}. New Account Balance: {account_data.get_balance()}')
                
        elif menuOption == '1':
            selection = acct_check()
            account_data = bank.get_account(selection)
            deposit = value_check_deposit()
            account_data.deposit(deposit)   # update account with deposit
            print(f'Deposited ${deposit}. New Account Balance: {account_data.get_balance()}')

    print('Goodbye!') 
    
if __name__=='__main__':
    main()





