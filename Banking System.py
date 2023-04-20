print("*"*50)

customernames=['anand','vicky','jai','bond','srinu']
customerpins=['1234','5678','9012','3456','1556']
customerbalance=[1000,2000,3000,4000,5000]
deposit=0
withdraw=0
balance=0
counter1=1
counter2=5
i=0
# This statement run continuously
while True:
    a='''
    ************************************************
    ---------------Welcome Big Bank-----------------
    ************************************************

    =====================MENU=======================

    <<<<<<        1.Open a New Account         >>>>>
    <<<<<<        2.Amount Withdraw            >>>>>
    <<<<<<        3.Amount Deposit             >>>>>
    <<<<<<        4.Check Customers & Balance  >>>>>
    <<<<<<        5.Exit                       >>>>>
    '''
    print(a)
    # Takes the choice number from the user.
    choicenum=input("Enter the number from the menu : ")
    if choicenum =="1":
        print("choicenum 1 is selected by the customer")
        # The line below will take the no:of customers from the user.
        NOC=eval(input("Number of Customers : "))
        i=i+NOC
        # The if condition will restrict the number of new account to 5.
        if i>5:
            print("\n")
            print("Customer Registration Exceed or Account Registration too low")
            i=i-NOC
        else:
            # The while loop will run according to the no:of customers.
            while counter1<=i:
                name=input("Enter Fullname :")
                customernames.append(name)
                pin=str(input("Enter the new Pin :"))
                pin=str(input("Confirm the Pin :"))
                customerpins.append(pin)
                balance=0
                deposit=eval(input("Enter the amount deposit to start an account :"))
                balance=balance+deposit
                customerbalance.append(balance)
                print("\nName=",end=" ")
                print(customernames[counter2])
                print("Pin",end=" ")
                print(customerpins[counter2])
                print("Balance",end=" ")
                print(customerbalance[counter2],end=" ")
                print("-/Rs")
                counter1=counter1+1
                counter2=counter2+1
                print("\nYour name is added")
                print("Your pin is generated")
                print("Your balance is added in your account")
                print("----Account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customernames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
                # This statement below helps the user to go back to the start of the program (menu).
        menu = input("Please press enter key to go back to menu to perform another function or exit ...")
    elif choicenum == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
        # This while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name = input("Please Enter name : ")
            pin = input("Please Enter pin : ")
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(customernames) - 1:
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name == customernames[k]:
                    if pin == customerpins[k]:
                        j = j + 1
                        # These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(customerbalance[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerbalance[k])
                        # Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input("Input value to Withdraw : "))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if withdrawal > balance:
                            # This statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerbalance[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - withdrawal
                            # These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerbalance[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                # The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choicenum == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(customernames) - 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name == customernames[k]:
                    if pin == customerpins[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(customerbalance[k], end=" ")
                        print("-/Rs")
                        balance = (customerbalance[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition # 1000+500=1500
                        customerbalance[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choicenum == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customernames) - 1:
            print("->.Customer =", customernames[k])
            print("->.Balance =", customerbalance[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choicenum == "5":
        # These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")


