# Alec Porter Lab 2 Part 2

# request input from user:  starting weight and how much they want to lose per month
startWeight = float(input('Enter your starting weight (in lbs): '))
weightLossPerMonth = float(input('Enter how much weight you want to lose per month (in lbs): '))

# initialize values
numOfMonths = 6
targetWeight = startWeight

# print table header
print('\n{0:<}\t| {1:<}'.format('Month','Target Weight'))
print('-----------------------')

# print table
for n in range(1,numOfMonths+1):
    targetWeight -= weightLossPerMonth
    print('{0:<}\t| {1:.1f}'.format(n,targetWeight))

# print total weight loss
print('\nYou\'re going to lose {0:.1f} pounds over the next {1} months!\nYou got this!'.format(weightLossPerMonth*numOfMonths,numOfMonths))
