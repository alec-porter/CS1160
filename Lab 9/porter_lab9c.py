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

def acct_check():
    isValid = False
    while not isValid:
        selection = str(input('Enter Your Accout Number: '))
        validation = bank.get_account(selection)
        if validation == None:
            print('You did not enter a valid account number, try again.')
            isValid = False
        else:
            isValid = True
            return selection
        



class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

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

    def add_account(self, account):
        account_number = BankAccount.get_account_number(account)
        self.__accounts[account_number]=account
        return self.__accounts
                        
    def get_account(self, account_number):
        for n, details in self.__accounts.items():
            if account_number == n:
                print('Retrieved Account Number {0}'.format(account_number))
                return details

    def list_accounts(self):
        print(self.__accounts)
        print('\nList of Accounts:')
        for n, details in self.__accounts.items():
            holder_name = BankAccount.get_holder_name(details)
            print('Account Number: {0}, Holder Name: {1}'.format(n, holder_name))
                       
    def display_account_info(self, account_number):
        for n, details in self.__accounts.items():
            if account_number == n:
                holder_name = BankAccount.get_holder_name(details)
                account_number = BankAccount.get_account_number(details)
                balance = BankAccount.get_balance(details)
                print('Account Number: {0}, Holder Name: {1}, Account Balance: {2}'.format(account_number, holder_name, balance))

        
      
# initialize accounts
bankaccount1 = BankAccount('001','Alec',2500.25)
bankaccount2 = BankAccount('002','Bob',500.00)
bankaccount3 = BankAccount('003','Sue',15500.75)
# add BankAccount objects to bank
bank = Bank()
bank.add_account(bankaccount1)
bank.add_account(bankaccount2)
bank.add_account(bankaccount3)

#bank.display_account_info('002')
details = bank.get_account('003')
print(details == None)


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
            bank.list_accounts()


            


        


if __name__=='__main__':
    main()



