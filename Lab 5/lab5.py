# Alec Porter
# Lab 5


# Functions -----------------------------------------------------------------------------------------------

# addition funciton 
def addNums():
    value1 = float(input('Enter the first number in the operation: '))
    value2 = float(input('Enter the second number in the operation: '))
    finalValue = value1 + value2
    print('{0} + {1} = {2}\n'.format(value1, value2, finalValue))

# subtraction function 
def subtractNums():
    value1 = float(input('Enter the first number in the operation: '))
    value2 = float(input('Enter the second number in the operation: '))
    finalValue = value1 - value2
    print('{0} - {1} = {2}\n'.format(value1, value2, finalValue))

# multiplication function 
def multNums():
    value1 = float(input('Enter the first number in the operation: '))
    value2 = float(input('Enter the second number in the operation: '))
    finalValue = value1 * value2
    print('{0} * {1} = {2}\n'.format(value1, value2, finalValue))

# division function 
def divNums():
    value1 = float(input('Enter the first number in the operation: '))
    value2 = float(input('Enter the second number in the operation: '))
    finalValue = value1 / value2
    print('{0} / {1} = {2}\n'.format(value1, value2, finalValue))

# modulo function 
def modNums():
    value1 = float(input('Enter the first number in the operation: '))
    value2 = float(input('Enter the second number in the operation: '))
    finalValue = value1 % value2
    print('{0} % {1} = {2}\n'.format(value1, value2, finalValue))



# Main Program ---------------------------------------------------------------------------------------------

def main():
    print('Welcome to my calculator!  Here are the following choices:')
    print('a - addition')
    print('s - subtraction')
    print('m - multiplication')
    print('d - division')
    print('o - modulo')
    print('q - quit program\n')

    # initialize variables
    userInput=''

    # request user input
    while userInput != 'q':
        userInput = str(input('Enter the mathmatical operation [a, s, m, d, o, q]: '))

        
        # verify user input is valied
        while userInput != 'a' and userInput != 's' and userInput != 'm' and userInput != 'd' and userInput != 'o' and userInput != 'q':
            print('Invalid Input')
            userInput = str(input('Enter the mathmatical operation [a, s, m, d, o, q]: '))
        
        if userInput == 'a':
            addNums()
        elif userInput == 's':
            subtractNums()
        elif userInput == 'm':
            multNums()
        elif userInput == 'd':
            divNums()
        elif userInput == 'o':
            modNums()
              
    print('Thank you for using the calculator!')


if __name__=="__main__":
    main()


