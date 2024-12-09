# Alec Porter Lab 9

# Functions ---------------------------------------------------------

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
         
# check for valid account number
def acct_check():
    isValid = False
    while not isValid:
        selection = str(input('Enter Your Account Number: '))
        if account.get_account(selection)[selection]==None:
            print('You did not enter a valid account number, try again.')
            isValid = False
        else:
            isValid = True
            return selection
   
        
# Classes -----------------------------------------------------------

class BankAccount:
    def __init__(self, x, y, z):
        self.__account_num = x
        self.__holder_name = y
        self.__balance = z

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdrawl(self, amount):
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def display_account_info(self):
        return f'Account Information - Account Number: {self.__account_number}, Account Holder: {self.__holder_name}, Account Balance: ${self.__balance}'


class Bank:
    def __init__(self):
        self.__accounts = {}

    def add_account(self, account):     # bring in account info from BankAccout and create accounts dictionary
        self.__accounts[account[0]]={'Name': account[1], 'Balance': account[2]}
        return f'Added Account Number {account[0]} belonging to {account[1]} with a balance of {account[2]}.'
    
    def get_account(self, account_number):  # returns account information in dictionary form
        return {account_number: self.__accounts.get(account_number)}

    def list_accounts(self):        # print list of account numbers and account owners
        for n, details in self.__accounts.items():
            print('Account Number: {0}, Holder Name: {1}'.format(n, details['Name']))
        
    def display_account_info(self, account_number):     # print account details of specific account
        print('Account Number: {0}, Holder Name: {1}, Account Balance: {2}'.format(account_number, self.__accounts[account_number]['Name'], self.__accounts[account_number]['Balance']))
        

# initialize bank accounts 
account1 = ['001','Alec',2500.25]
account2 = ['002','Bob',500.00]
account3 = ['003','Sue',15500.75]

# add accounts to bank
account = Bank()
account.add_account(account1)
account.add_account(account2)
account.add_account(account3)

# test block
print('\ntest code here:')


print('end test\n')

# Main Program ------------------------------------------------------

def main():

    # initialize menu loop
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
            print('List of accounts:')
            account.list_accounts()

        if menuOption == '3':
            acctCheck = acct_check()
            x = account.get_account(acctCheck)
            print(x)
            bankaccount = BankAccount()
            print(bankaccount.get_balance())


        


if __name__=='__main__':
    main()
