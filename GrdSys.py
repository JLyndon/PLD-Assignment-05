import math
import time
def Rounder_(InputGrade):
    if "." not in InputGrade:
        return int(InputGrade)
    else:
        whole, decimal = InputGrade.split(".")
        if (int(decimal) >= 0):
            if int(decimal[0]) >= 5:
                roundedup_equival = math.ceil(float(InputGrade))
                return roundedup_equival
            elif int(decimal[0]) < 5:
                roundeddown_equival = math.floor(float(InputGrade))
                return roundeddown_equival
        elif (int(decimal) == 0):
            return whole

def GradeClassifier(GradeReference):
    if GradeReference >= 97 and GradeReference <= 100:
        return print("Grade/Mark: 1.0\nDescription: Excellent")
    elif GradeReference >= 94 and GradeReference <= 96:
        return print("Grade/Mark: 1.25\nDescription: Excellent")
    elif GradeReference >= 91 and GradeReference <= 93:
        return print("Grade/Mark: 1.50\nDescription: Very Good")
    elif GradeReference >= 88 and GradeReference <= 90:
        return print("Grade/Mark: 1.75\nDescription: Very Good")
    elif GradeReference >= 85 and GradeReference <= 87:
        return print("Grade/Mark: 2.0\nDescription: Good")
    elif GradeReference >= 82 and GradeReference <= 84:
        return print("Grade/Mark: 2.25\nDescription: Good")
    elif GradeReference >= 79 and GradeReference <= 81:
        return print("Grade/Mark: 2.5\nDescription: Satisfactory")
    elif GradeReference >= 76 and GradeReference <= 78:
        return print("Grade/Mark: 2.75\nDescription: Satisfactory")
    elif GradeReference == 75:
        return print("Grade/Mark: 3.0\nDescription: Passing")
    elif GradeReference >= 65 and GradeReference <= 74:
        return print("Grade/Mark: 5.0\nDescription: Failure")
    else:
        return print(f"The rating is unavailable for the grade {init_grade}.")

def UnivGradeClassifier(FlatGrade, Decimals):
    if FlatGrade == "1":
        if (Decimals == None) or (int(Decimals) == 0):
            print("Percentage Range: 97-100\nDescription: Excellent")
        elif Decimals == "25":
            print("Percentage Range: 94-96\nDescription: Excellent")
        elif (Decimals == "50") or (Decimals == "5"):
            print("Percentage Range: 91-93\nDescription: Very Good")
        elif Decimals == "75":
            print("Percentage Range: 88-90\nDescription: Very Good")
    elif FlatGrade == "2":
        if (Decimals == None) or (int(Decimals) == 0):
            print("Percentage Range: 85-89\nDescription: Good")
        elif Decimals == "25":
            print("Percentage Range: 79-81\nDescription: Good")
        elif (Decimals == "50") or (Decimals == "5"):
            print("Percentage Range: 76-78\nDescription: Satisfactory")
        elif Decimals == "75":
            print("Percentage Range: 76-78\nDescription: Satisfactory")
    elif FlatGrade == "3":
        if (Decimals == None) or (int(Decimals) == 0):
            print("Percentage Range: 75\nDescription: Passing")
    elif FlatGrade == "5":
        if (Decimals == None) or (int(Decimals) == 0):
            print("Percentage Range: 65-74\nDescription: Failure")

def ValidationResponse(StringVal):
    if StringVal.lower() == "back":
        time.sleep(2)
        print("\n\nWelcome back to the Main Menu!\n\nPlease choose from the following actions:\nType\n1 - To check grades in scale of 1-100\n2 - To check grades in scale of 1.0-5.0\n3 - To view grades with specified Remarks\nexit - To exit the program")
        return "return_menu"
    elif StringVal.replace(".","").lower() == "inc":
        return print("Percentage Range: N/A\nDescription: Incomplete")
    elif StringVal.replace(".","").upper() == "W":
        return print("Percentage Range: N/A\nDescription: Withdrawn")
    elif StringVal.replace(".","").upper() == "D":
        return print("Percentage Range: N/A\nDescription: Dropped")
    elif StringVal.isalpha() == True:
        return print("Please enter a numeric value.")
    elif StringVal.isalnum() == True:
        return print("Inputs must be numbers only.")
    else:
        return print("Please enter a valid input.")

def DecisionMenu():
    global init_grade
    print("Welcome to Grade Checker!\n\nPlease choose from the following actions:\nType\n1 - To check grades in scale of 1-100\n2 - To check grades in scale of 1.0-5.0\n3 - To view grades with specified Remarks\nexit - To exit the program")
    while True:
        Usr_decision = input("\n> ")
        if Usr_decision == "1":
            print("Type 'back' - To return to the main menu")
            while True:
                init_grade = input("\nEnter Grade: ")
                if init_grade.replace(".","").isdecimal() == True:
                    GradeClassifier(Rounder_(init_grade))
                else:
                    if (ValidationResponse(init_grade)) == "return_menu":
                        break
                    else:
                        pass
        elif Usr_decision == "2":
            print("Type 'back' - To return to the main menu")
            while True:
                secon_grade = input("Enter Grade: ")
                if secon_grade.replace(".","").isdecimal() == True:
                    if "." not in secon_grade:
                        UnivGradeClassifier(secon_grade[-1], None)
                    else:
                        Whole, Fraction = secon_grade.split(".")
                        UnivGradeClassifier(Whole[0], Fraction[0:2])
                else:
                    if (ValidationResponse(secon_grade)) == "return_menu":
                        break
                    else:
                        pass
        elif Usr_decision == "3":
            tert_grade = input("Enter Grade: ")
        elif Usr_decision.lower() == "exit":
            print("Thank you for stopping by! Have a great day :)")
            break
    
DecisionMenu()

# program #2: grading
# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed