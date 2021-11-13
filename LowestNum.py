def Usr_inpt():
    Numb01 = int(input("Enter first number: "))
    Numb02 = int(input("Enter second number: "))
    Numb03 = int(input("Enter third number: "))
    return Numb01, Numb02, Numb03

#Accepts inputs with int val
def Get_lowest_(FNum, Snum, ThNum):
    if (FNum < Snum) and (FNum < ThNum):
        print(FNum)
    elif (Snum < FNum) and (Snum < ThNum):
        print(Snum)
    elif (ThNum < FNum) and (ThNum < Snum):
        print(ThNum)
    elif (ThNum == FNum) and (ThNum == Snum):
        print(FNum)
    else: #Accepts inputs with alike values and still solve for the lowest value
        if (FNum == Snum) or (FNum == ThNum):
            print(FNum)
        elif (Snum == FNum) or (Snum == ThNum):
            print(Snum)
        elif (ThNum == FNum) or (ThNum == Snum):
            print(ThNum)

First, Second, Third = Usr_inpt()
Get_lowest_(First, Second, Third)