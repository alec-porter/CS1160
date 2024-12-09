# Alec Porter Lab 8

# functions ------------------------------------------------------------------------------------------------------------------

def validatePlayerInputs():   # check player inputs
    isValid = False   # initialize check for valid input
    while not isValid:   
        try:
            rowGuess = int(input('Guess a row: '))
            colGuess = int(input('Guess a column: '))
            if rowGuess > 0 and rowGuess < 11 and colGuess > 0 and colGuess < 11:  # check for a valid row input and range
                isValid = True
            else:
                print('Your input was not in the range of the grid, try again!')
                isValid = False
        except ValueError:
            print('Your input was not a number, try again!')   # check for a valid integer input
            isValid = False
    return rowGuess, colGuess

def displayGrid(grid):   # format output
    print('{0:<3}  {1:<3} {2:<3} {3:<3} {4:<3} {5:<3} {6:<3} {7:<3} {8:<3} {9:<3} {10:<3}'.format('',1,2,3,4,5,6,7,8,9,10))
    print('-------------------------------------------')
    for n in range(0,10):
        print('{0:<3}| {1:<3} {2:<3} {3:<3} {4:<3} {5:<3} {6:<3} {7:<3} {8:<3} {9:<3} {10:<3}'.format(n+1,grid[n][0],grid[n][1],grid[n][2],grid[n][3],grid[n][4],grid[n][5],grid[n][6],grid[n][7],grid[n][8],grid[n][9]))
    
    

# main ------------------------------------------------------------------------------------------------------------------------

def main():
    print('Welcome to Battleship\n')
    print('X = Hit, - = Miss\n')
    player1 = str(input('Enter name for player 1: '))
    player2 = str(input('Enter name for player 2: '))

    player1Grid = (('B','B','B','B','B','0','0','0','0','0'),
                   ('0','0','0','0','0','0','0','B','B','0'),
                   ('0','0','B','0','0','0','0','B','B','0'),
                   ('0','0','B','0','0','0','0','0','0','0'),
                   ('0','0','B','0','0','0','0','0','0','0'),
                   ('0','0','B','0','0','0','B','0','0','0'),
                   ('0','0','0','0','0','0','B','0','B','0'),
                   ('0','0','0','0','0','0','B','0','0','0'),
                   ('0','0','0','0','0','0','0','0','B','0'),
                   ('0','0','0','0','0','0','0','0','0','0'))

    player2Grid = (('B','0','0','0','0','0','0','0','0','0'),
                   ('B','0','0','0','0','0','B','B','B','0'),
                   ('B','0','0','0','0','0','0','0','0','0'),
                   ('B','0','B','B','0','0','0','0','0','0'),
                   ('B','0','0','0','0','B','0','0','0','0'),
                   ('0','0','B','B','0','0','0','0','0','0'),
                   ('0','0','0','0','0','0','0','0','B','0'),
                   ('0','0','0','0','0','0','0','0','0','0'),
                   ('0','0','0','0','B','B','B','B','0','0'),
                   ('0','0','0','0','0','0','0','0','0','0'))

 #   player1Display = [['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0'],
 #                  ['0','0','0','0','0','0','0','0','0','0']]

    player1Display = [['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','','']]

#    player2Display = [['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0'],
#                   ['0','0','0','0','0','0','0','0','0','0']]

    player2Display = [['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','',''],
                   ['','','','','','','','','','']]

    



    
    
    # initialize variables for winning state
    noWinner = True   
    player1count = 0
    player2count = 0

    while noWinner == True:

        # player 1's turn -------------------------------------------------------------------
        print('\n{0}\'s Turn!'.format(player1))
        print('{0}\'s Previous Guesses: '.format(player1))

        displayGrid(player1Display)

        rowGuess, colGuess = validatePlayerInputs()   # check if user input valid coordinate

        while player1Display[rowGuess-1][colGuess-1] != '':   # check to see if coordinate already guessed
            print('You already guessed that coordinate!')
            rowGuess, colGuess = validatePlayerInputs()
        if player2Grid[rowGuess-1][colGuess-1] == 'B':   # if input matches B on opponent's grid it is a hit
            print('Good shot!  You hit your opponent\'s battleship')
            player1Display[rowGuess-1][colGuess-1] = 'X'    # update player's display
            player1count +=1
        else:
            print('You missed your opponent\'s battleship!')  # if input does not match B on opponent's grid it is a miss
            player1Display[rowGuess-1][colGuess-1] = '-'   # update player's display

        if player1count == 18:   # if player hit all targets, end game
            print('Player 1 Wins')
            break
            
        # player 2's turn -------------------------------------------------------------------
        print('\n{0}\'s Turn!'.format(player2))
        print('{0}\'s Previous Guesses: '.format(player2))

        displayGrid(player2Display)

        rowGuess, colGuess = validatePlayerInputs()   # check if user input valid coordinate

        while player2Display[rowGuess-1][colGuess-1] != '':   # check to see if coordinate already guessed
            print('You already guessed that coordinate!')
            rowGuess, colGuess = validatePlayerInputs()
        if player1Grid[rowGuess-1][colGuess-1] == 'B':   # if input matches B on opponent's grid it is a hit
            print('Good shot!  You hit your opponent\'s battleship')
            player2Display[rowGuess-1][colGuess-1] = 'X'    # update player's display
            player2count += 1
        else:
            print('You missed your opponent\'s battleship!')  # if input does not match B on opponent's grid it is a miss
            player2Display[rowGuess-1][colGuess-1] = '-'   # update player's display

        if player2count == 18:   # if player hit all targets, end game
            print('\nPlayer 2 Wins')
            break

    print('\nThank you for playing Battleship')



if __name__=='__main__':
    main()
