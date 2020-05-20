import Account
from Account import theAccount

# Prevents the program's termination
never = 0

# To keep track: new account created
count = 0
newAccount = []
checkSuccess = 0

# Keep the program running forever ("quit" is available for testing purposes)
while never == 0:
    # Main Screen
    print("\n----------------------------"
          "\n  Welcome to Shanghai Bank "
          "\n----------------------------\n")
    print("You can ")
    firstOption = input("> 1. create a new account \n"
                        "> 2. login to an already existing account \n"
                        "(Input the number) Your choice: ")

    # User decides to create a new account
    if firstOption == "1":
        print("\n ...  NEW ACCOUNT  ... \n"
              "You are about to create a new account. \n"
              "Please input all the required information.")
        myName = input("Your full name (last, first): ")
        myBirthday = input("Your birthday (month/day/year): ")
        myID = input("Create an ID for your account: ")
        myPassword = input("Create a password to secure your account: ")
        newAccount.append(theAccount(myID, myPassword, myName, myBirthday))
        count += 1
        print("You have successfully created a new account.")


    # User decides to log into an account
    elif firstOption == "2":
        print("\n ...  LOGIN  ...")
        enterID = input("Enter your ID: ")
        enterPassword = input("Enter your password: ")
        for each in newAccount:
            if each.ID == enterID and each.password == enterPassword:
                print("\n  ...  \n logging in \n  ...")
                Account.myAccount_Screen(each)
                checkSuccess += 1
            else:
                continue
        if checkSuccess == 0:
            print("You have entered an invalid ID or an incorrect password.")
        else:
            checkSuccess == 0

    # User decides to quit the program (hidden option)
    elif firstOption == "quit":
        never += 1

    else:
        print("Wrong input. Please try again.")