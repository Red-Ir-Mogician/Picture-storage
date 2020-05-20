#Felix Han
#2020/5/20
#quic

class theAccount:
    def __init__(self,myID, myPassword, myName, myBirthday):
        self.ID = myID
        self.password = myPassword
        self.name = myName
        self.mybirthday = myBirthday
        self.money = 0

def myAccount_Screen(objeat):
    while True:
        print('Hi %s,\nYour have %s in Your Account' % (objeat.name,str(objeat.money)))
        choose = input("> 1. deposit(put in) money \n"
                        "> 2. retrieve(take out) the money \n"
                       '> 3. change account \n'
                        "(Input the number) Your choice: ")
        if choose == '1':
            try:
                choose = float(input('Place input how much you want deposit:'))
                objeat.money += choose
            except:
                print('input a NUMBLE!!!!!!!!')

        if choose == '2':
            try:
                choose = float(input('Place input how much you want deposit:'))
                if choose <= objeat.money:
                    objeat.money -= choose
                else:
                    print('Your do not have money in your account')
            except:
                print('input a NUMBLE!!!!!!!!')

        if choose == '3':
            break

        else:
            print("Wrong input. Please try again.")