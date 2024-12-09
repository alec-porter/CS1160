# Alec Porter Lab 7


def main():

    print('Welcome to the YMCA Database\n')

    # initialize variables
    addAnother = 'y'
    memberList = []
    activeMemberIncome = []

    while addAnother == 'y':
        
        # input first and last name
        firstName = str(input('Frist Name: '))
        lastName = str(input('Last Name: '))

        # age validation check
        try:
            age = int(input('Age: '))
            restart = False
        except ValueError:
            print('Age was invalid, please enter member\'s data again.')
            restart = True
        if restart == True:
            continue

        # active member validation check
        account = str(input('User\'s Account is Active: '))
        if account == 'True':
            activeAccount = True
        elif account == 'False':
            activeAccount = False
        else:
            print('Active was invalid, please enter member\'s data again.')
            continue       
                            
        # bill validation check
        try:
            bill = float(input('Monthly Bill: $'))
            restart = False
        except ValueError:
            print('Bill was invalid, please enter member\'s data again')
            restart = True
        if restart == True:
            continue            
               

        memberList.append([firstName, lastName, age, activeAccount, bill])  # append member list with inputs

        if activeAccount == True:  # add active member bill to income list
            activeMemberIncome.append(bill)        

        # add additional member validation check
        addAnother = input('Would you like to enter another YMCA member (y/n): ')
        while addAnother != 'y' and addAnother != 'n':
            addAnother = input('Error, enter y or n.  Would you like to enter another YMCA member (y/n): ')
        


    # print result header
    print('\n-----------Current YMCA Membership Data-----------')
    print('|{0:<20} |{1:<4} |{2:<8} |{3:}'.format('Name:', 'Age:', 'Active:', 'Bill:'))
    print('----------------------------------------------------')
    for n in memberList:
          print('|{0:<20} |{1:<4} |{2:<8} |${3:.2f}'.format(n[1]+ ', '+ n[0], n[2], str(n[3]), n[4]))
        
    
    # calculate totals/averages for revenue and member numbers then print data
    print('\n--------------------Statistics--------------------')
    try:  
        averageRevenue = sum(activeMemberIncome)/len(activeMemberIncome)  
        print('Total Revenue from Active Members: ${0:.2f}'.format(sum(activeMemberIncome)))
        print('Average Revenue from Active Members: ${0:.2f}'.format(averageRevenue))
    except:
        print('No Active Members, Revenue is $0.00')
    print('Total Number of Members: {0}'.format(len(memberList)))
    print('Total Number of Active Members: {0}'.format(len(activeMemberIncome)))
        
   
if __name__=='__main__':
    main()
