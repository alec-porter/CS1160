# Alec Porter - Lab 6

# Functions --------------------------------------------------------------------------------------------

def inputFunction():     # user input function
    isValid = False     # initialize excpetion to check if user input a number
    while not isValid:      # check if user input number, if not, loop until they do
        try:
            value1 = float(input('Enter the first number: '))
            isValid = True
        except ValueError:
            print('That was not a number.')
            isValid = False
    isValid = False     # initialize excpetion to check if user input a number
    while not isValid:     # check if user input number, if not, loop until they do
        try:     
            value2 = float(input('Enter the second number: '))
            isValid = True
        except ValueError:
            print('That was not a number.')
            isValid = False
    return value1, value2


def addNums(value1, value2):     # addition function
    finalValue = value1 + value2
    print('{0} + {1} = {2}'.format(value1, value2, finalValue))
    return finalValue


def subtractNums(value1, value2):     # subtraction function
    finalValue = value1 - value2
    print('{0} - {1} = {2}'.format(value1, value2, finalValue))
    return finalValue


def multNums(value1, value2):     # multiplication function
    # caluclate, print, and return value
    finalValue = value1 * value2
    print('{0} * {1} = {2}'.format(value1, value2, finalValue))
    return finalValue

def divNums(value1, value2):     # dividion function
    try:   # check for divide by zero and output error message if divide by zero
        finalValue = value1 / value2
        print('{0} / {1} = {2}'.format(value1, value2, finalValue))
    except ZeroDivisionError:
        print('Error - {0} / {1} is division by zero'.format(value1, value2))
        finalValue = 'Error - Divide by Zero'
    return finalValue

def modNums(value1, value2):     # modulo function
    finalValue = value1 % value2
    print('{0} % {1} = {2}'.format(value1, value2, finalValue))
    return finalValue

def inputFile():     # read from file function
    isValid = False     # initialize exception to check if user entered a valid filename
    while not isValid:
        try:     # check if user input valid filename, if not, loop until they do
            fileName = input('Enter the name of the file: ')
            mathFileInput = open(fileName,'r')
            mathFileOutput = open('output.txt','w')
            isValid = True
        except FileNotFoundError:
            print('That file does not exist, try again.')
            isValid = False
    mathType = '0'     # initialize readline
    while mathType !='':
        mathType = mathFileInput.readline().rstrip()
        # check for type of math required, call math function, and write to file
        if mathType == 'a':
            value1 = float(mathFileInput.readline().rstrip())
            value2 = float(mathFileInput.readline().rstrip())
            finalValue = addNums(value1, value2)
            mathFileOutput.write(str(finalValue)+'\n')
        elif mathType == 's':
            value1 = float(mathFileInput.readline().rstrip())
            value2 = float(mathFileInput.readline().rstrip())
            finalValue = subtractNums(value1, value2)
            mathFileOutput.write(str(finalValue)+'\n')
        elif mathType == 'm':
            value1 = float(mathFileInput.readline().rstrip())
            value2 = float(mathFileInput.readline().rstrip())
            finalValue = multNums(value1, value2)
            mathFileOutput.write(str(finalValue)+'\n')
        elif mathType == 'd':
            value1 = float(mathFileInput.readline().rstrip())
            value2 = float(mathFileInput.readline().rstrip())
            finalValue = divNums(value1, value2)
            mathFileOutput.write(str(finalValue)+'\n')
        elif mathType == 'o':
            value1 = float(mathFileInput.readline().rstrip())
            value2 = float(mathFileInput.readline().rstrip())
            finalValue = modNums(value1, value2)
            mathFileOutput.write(str(finalValue)+'\n')
    mathFileInput.close()        
    mathFileOutput.close()
    
            
        
            
        
        
            
# Main Program ---------------------------------------------------------------------------------------------

def main():
    print('Welcome to my calculator!  Here are the following choices:')
    print('a - addition')
    print('s - subtraction')
    print('m - multiplication')
    print('d - division')
    print('o - modulo')
    print('i - input file')
    print('q - quit program')

    # initialize variables
    userInput=''

    # request user input
    while userInput != 'q':
        userInput = str(input('\nEnter the mathmatical operation [a, s, m, d, o, i, q]: '))

        
        # verify user input is valied
        while userInput != 'a' and userInput != 's' and userInput != 'm' and userInput != 'd' and userInput != 'o' and userInput != 'i' and userInput != 'q':
            print('Invalid Input')
            userInput = str(input('\nEnter the mathmatical operation [a, s, m, d, o, q]: '))

        # run corresponding math function
        if userInput == 'a':
            value1, value2 = inputFunction()
            addNums(value1, value2)
        elif userInput == 's':
            value1, value2 = inputFunction()
            subtractNums(value1, value2)
        elif userInput == 'm':
            value1, value2 = inputFunction()
            multNums(value1, value2)
        elif userInput == 'd':
            value1, value2 = inputFunction()
            divNums(value1, value2)
        elif userInput == 'o':
            value1, value2 = inputFunction()
            modNums(value1, value2)
        elif userInput == 'i':
            inputFile()
              
    print('Thank you for using the calculator!')


if __name__=="__main__":
    main()
    
    
    


