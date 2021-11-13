def Usr_inpt():
    while True: #Added conditions for input validation. Accepts decimal inputs.
        while True:
            Numb01 = input("\nEnter first number: ")
            if Numb01.replace(".","").isdigit() == True:
                Fnl_01 = float(Numb01)
                pass
                while True:
                    Numb02 = input("Enter second number: ")
                    if Numb02.replace(".","").isdigit() == True:
                        Fnl_02 = float(Numb02)
                        pass
                        while True:
                            Numb03 = input("Enter third number: ")
                            if Numb03.replace(".","").isdigit() == True:
                                Fnl_03 = float(Numb03)
                                return Fnl_01, Fnl_02, Fnl_03
                            else:
                                print("Enter valid characters.")
                    else:
                        print("Enter valid characters.")
            else:
                print("Enter valid characters.")

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