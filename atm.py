class ATM:

    def __init__(self):

        self.__pin=6380
        self.__balance=5000

    def withdraw(self,pas,amount):

        if self.__pin == pas:

            if amount <= self.__balance:

                self.__balance -=amount
                print("withdraw successfully")

                return self.__balance
        else:
            print("invalid Pin")
            
    def deposit(self,pas,amount):

        if self.__pin ==pas:

            if amount >0:

                self.__balance +=amount
                print("deposit successfully")

                return self.__balance
        else:
            print("invalid pin")
    def show_balance(self):

        print("the balance amount",self.__balance)

    def update_pin(self,old,pas):

        if old ==self.__pin:

            self.__pin ==pas

            return self.__pin
        else:
            print("enter correct old PIN")

            
data=ATM()
print("1.withdraw")
print("2.deposit")
print("3.show balance")
print("4.update PIN")
while True:

    choice=int(input("enter the choice"))

    if choice ==1:
        pas=int(input("enter the PIN"))
        amount=int(input("enter the amount"))

        data.withdraw(pas,amount)
    elif choice ==2:
        pas=int(input("enter the PIN"))
        amount=int(input("enter the amount"))

        data.deposit(pas,amount)

    elif choice ==3:
        data.show_balance()
    elif choice==4:
        old=int(input("enter the old PIN"))
        pas=int(input("enter the new PIN"))
        data.update_pin(old,pas)

    elif choice ==5:
        break

