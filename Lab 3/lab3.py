# Alec Porter Lab 3
# Write a program that requests 5 grades from the user, computes the average grade, then tells the user their average and corresponding letter grade.
# You can assume the user will always enter grades between 0.00 to 100.00.

print('Welcome to the grade estimator.')

# iniitialize values
totalgrade = 0


# request five grades from user and calulate the total value of the five grades
for gradeinput in range(1,6):
    gradeinput = float(input('Please enter your grade for assignment {0}: '.format(gradeinput)))
    totalgrade = totalgrade + gradeinput

# calculate and display average
averagegrade = totalgrade/5
print('Your average grade is {0:.2f}.'.format(averagegrade))

# determine letter grade based on average grade and outlput letter grade received
if averagegrade>=90.00:
    print('You will get an A in this class.')
elif averagegrade<90.00 and averagegrade>=80.00:
    print('You will get a B in this class.')
elif averagegrade<80.00 and averagegrade>=70.00:
    print('You will get a C in this class.')
elif averagegrade<70.00 and averagegrade>=60.00:
    print('You will get a D in this class.')
else:
    print('You will get a F in this class.')
