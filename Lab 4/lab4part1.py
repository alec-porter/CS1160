# Alec Porter Lab 2 Part 1

# Initialize values
anotherGrade = 'y'
totalGrade = 0
countAssignment = 0

# request user input grade and continue loop if y is entered
print('Welcome to the grade estimator.')
while anotherGrade == 'y':
    countAssignment += 1
    gradeInput = float(input('\nPlease enter your grade for assigment {0}: '.format(countAssignment)))
    totalGrade = totalGrade + gradeInput
    anotherGrade = input('Would you like to enter another grade? (y/n): ')
    
    
# calculate and display average
averageGrade = totalGrade / countAssignment
print('\nYour average grade is {0:.2f}.'.format(averageGrade))

# determine letter grade based on average grade and outlput letter grade received
if averageGrade>=90.00:
    print('You will get an A in this class.')
elif averageGrade<90.00 and averageGrade>=80.00:
    print('You will get a B in this class.')
elif averageGrade<80.00 and averageGrade>=70.00:
    print('You will get a C in this class.')
elif averageGrade<70.00 and averageGrade>=60.00:
    print('You will get a D in this class.')
else:
    print('You will get a F in this class.')
