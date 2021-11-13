def CommaReader_Single(StringVal):
    if "," in StringVal:
        CommaOmmi = StringVal.replace(",","")
        return CommaOmmi
    else:
        return StringVal

def Usr_inpt():
    while True: #Added conditions for input validation. Accepts decimal inputs.
        while True:
            Numb01 = input("\nEnter first number: ")
            DCNumb01 = CommaReader_Single(Numb01)
            if DCNumb01.replace(".","").isdigit() == True:
                Fnl_01 = float(DCNumb01)
                while True:
                    Numb02 = input("\nEnter second number: ")
                    DCNumb02 = CommaReader_Single(Numb02)
                    if DCNumb02.replace(".","").isdigit() == True:
                        Fnl_02 = float(DCNumb02)
                        while True:
                            Numb03 = input("\nEnter third number: ")
                            DCNumb03 = CommaReader_Single(Numb03)
                            if DCNumb03.replace(".","").isdigit() == True:
                                Fnl_03 = float(DCNumb03)
                                return Fnl_01, Fnl_02, Fnl_03
                            else:
                                print("Enter valid characters.")
                    else:
                        print("Enter valid characters.")
            else:
                print("Enter valid characters.")

def Get_lowest_(FNum, Snum, ThNum):
    if (FNum < Snum) and (FNum < ThNum):
        return FNum
    elif (Snum < FNum) and (Snum < ThNum):
        return Snum
    elif (ThNum < FNum) and (ThNum < Snum):
        return ThNum
    elif (ThNum == FNum) and (ThNum == Snum):
        return FNum
    else: #Accepts inputs with alike values and still solve for the lowest value
        if (FNum == Snum) or (FNum == ThNum):
            return FNum
        elif (Snum == FNum) or (Snum == ThNum):
            return Snum
        elif (ThNum == FNum) or (ThNum == Snum):
            return ThNum

First, Second, Third = Usr_inpt()
LowestVal = str(Get_lowest_(First, Second, Third))

wholeVal, fractionVal = LowestVal.split(".")

if int(fractionVal) == 0:
    print(f"\n{wholeVal:,}")
elif int(fractionVal) > 0:
    Fnl_LowestVal = float(LowestVal)
    print(f"\n{Fnl_LowestVal:,}")