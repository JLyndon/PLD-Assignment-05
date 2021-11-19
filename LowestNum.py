def CommaReader_Single(StringVal): #Remodeled version of previous CommaReader code block.
    if "," in StringVal:
        CommaOmmi = StringVal.replace(",","")
        return CommaOmmi
    else:
        return StringVal

def Validation(UsrInput): #Input Validation Statements
    if UsrInput.isalpha() == True:
        return print("Input must be a number.")
    elif UsrInput.isdigit() == True:
        return print("Input must be in numerical form.")
    elif UsrInput.isalnum() == True:
        return print("Input must only be numbers.")
    elif (UsrInput == "") or (UsrInput == None):
        return print("Please enter a number.")
    elif UsrInput.isspace() == True:
        return print("Please fill all the blanks.")
    else:
        print("Please enter a valid input.")

def Usr_inpt():
    while True: #Added conditions for input validation. Accepts decimal inputs.
        while True:
            Numb01 = input("\nEnter first number: ") #Accepts 'with comma' inputs. 
            DCNumb01 = CommaReader_Single(Numb01) #Checks for comma and omit for further processing.
            if DCNumb01.replace(".","").replace("-","").isdecimal() == True: 
                Fnl_01 = float(DCNumb01)
                while True:
                    Numb02 = input("\nEnter second number: ")
                    DCNumb02 = CommaReader_Single(Numb02)
                    if DCNumb02.replace(".","").replace("-","").isdecimal() == True:
                        Fnl_02 = float(DCNumb02)
                        while True:
                            Numb03 = input("\nEnter third number: ")
                            DCNumb03 = CommaReader_Single(Numb03)
                            if DCNumb03.replace(".","").replace("-","").isdecimal() == True:
                                Fnl_03 = float(DCNumb03)
                                return Fnl_01, Fnl_02, Fnl_03
                            else:
                                Validation(DCNumb03)
                    else:
                        Validation(DCNumb02)
            else:
                Validation(DCNumb01)

def Get_lowest_(FNum, Snum, ThNum):
    if (FNum < Snum) and (FNum < ThNum):
        return FNum
    elif (Snum < FNum) and (Snum < ThNum):
        return Snum
    elif (ThNum < FNum) and (ThNum < Snum):
        return ThNum
    elif (ThNum == FNum) and (ThNum == Snum):
        return FNum
    else: #Accepts inputs with alike values and still solve for the lowest value.
        if (FNum == Snum) or (FNum == ThNum):
            return FNum
        elif (Snum == FNum) or (Snum == ThNum):
            return Snum
        elif (ThNum == FNum) or (ThNum == Snum):
            return ThNum

First, Second, Third = Usr_inpt()
LowestVal = str(Get_lowest_(First, Second, Third))

wholeVal, fractionVal = LowestVal.split(".") #Splits the string into two.

if int(fractionVal) == 0: #Statements that evaluate the eligibility for display.
    if (wholeVal.replace("-","").__len__()) >= 4:
        print(f"\n{wholeVal:,}")
    else:
        print(f"\nThe lowest value of the three is '{wholeVal}'")
elif int(fractionVal) > 0:
    Fnl_LowestVal = float(LowestVal)
    print(f"\nThe lowest value of three is '{Fnl_LowestVal:,}'")