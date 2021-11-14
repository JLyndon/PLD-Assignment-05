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
    elif GradeReference > 100:
        return print(f"Grades are capped at 100. Please enter values within range.")
    else:
        return print(f"There's no available rating for the grade of '{init_grade}'")

def UnivGradeClassifier(FlatGrade, Decimals):
    if (int(FlatGrade) >= 0) and (int(FlatGrade) <= 5):
        if FlatGrade == "1":
            if (Decimals == None) or (int(Decimals) == 0):
                print("Percentage Range: 97-100\nDescription: Excellent")
            elif Decimals == "25":
                print("Percentage Range: 94-96\nDescription: Excellent")
            elif (Decimals == "50") or (Decimals == "5"):
                print("Percentage Range: 91-93\nDescription: Very Good")
            elif Decimals == "75":
                print("Percentage Range: 88-90\nDescription: Very Good")
            else:
                return print(f"There's no available rating for the grade of '{secon_grade}'")
        elif FlatGrade == "2":
            if (Decimals == None) or (int(Decimals) == 0):
                print("Percentage Range: 85-87\nDescription: Good")
            elif Decimals == "25":
                print("Percentage Range: 82-84\nDescription: Good")
            elif (Decimals == "50") or (Decimals == "5"):
                print("Percentage Range: 79-81\nDescription: Satisfactory")
            elif Decimals == "75":
                print("Percentage Range: 76-78\nDescription: Satisfactory")
            else:
                return print(f"There's no available rating for the grade of '{secon_grade}'")
        elif FlatGrade == "3":
            if (Decimals == None) or (int(Decimals) == 0):
                print("Percentage Range: 75\nDescription: Passing")
            else:
                return print(f"There's no available rating for the grade of '{secon_grade}'")
        elif FlatGrade == "5":
            if (Decimals == None) or (int(Decimals) == 0):
                print("Percentage Range: 65-74\nDescription: Failure")
            else:
                return print(f"There's no available rating for the grade of '{secon_grade}'")
        else:
            return print(f"There's no available rating for the grade of '{secon_grade}'")
    elif (int(FlatGrade) < 0) or (int(FlatGrade) > 5):
        return print("The Grading System has its standard scale (1.0-3.0 & 5.0). Please, be guided accordingly.")

def RemarksGradeEquival(RemarkReference):
    if RemarkReference == "Excellent":
        return print("\n'Excellent' Remarks can be earned by obtaining a grade within:\nPercentage Range: 94-100\nGrades/Mark: 1.25-1.0")
    elif RemarkReference == "Very Good":
        return print("\n'Very Good' Remarks can be earned by obtaining a grade within:\nPercentage Range: 88-93\nGrades/Mark: 1.5-1.75")
    elif RemarkReference == "Good":
        return print("\n'Good' Remarks can be earned by obtaining a grade within:\nPercentage Range: 82-87\nGrades/Mark: 2.25-2.0")
    elif RemarkReference == "Satisfactory":
        return print("\n'Satisfactory' Remarks can be earned by obtaining a grade within:\nPercentage Range: 76-81\nGrades/Mark: 2.50-2.75")
    elif RemarkReference == "Passing":
        return print("\n'Passing' Remarks can be earned by obtaining a grade of:\nPercentage: 75\nGrades/Mark: 3.0")
    elif RemarkReference == "Failure":
        return print("\n'Failure' Remarks can be earned by obtaining a grade of:\nPercentage Range: 65-74\nGrades/Mark: 5.0")
    elif RemarkReference.replace(".","") == "Incomplete":
        return print("Percentage Range: N/A\nGrades/Mark: Inc")
    elif RemarkReference.replace(".","") == "Withdrawn":
        return print("Percentage Range: N/A\nGrades/Mark: W")
    elif RemarkReference.replace(".","") == "Dropped":
        return print("Percentage Range: N/A\nGrades/Mark: D")
    else:
        return print(f"There's no equivalent rating for '{RemarkReference}'")
    
def ValidationResponse(StringVal):
    if StringVal.lower() == "back":
        time.sleep(2)
        print("\n\nWelcome back to the Main Menu!\n\nPlease choose from the following actions:\nType\n1 - To check grades in scale of 1-100\n2 - To check grades in scale of 1.0-5.0\n3 - To view grades with specified Remarks\nexit - To exit the program")
        return "return_menu"
    elif StringVal.replace("-","").replace(".","").isdigit() == True:
        print("Grades are all positive. Please enter a postive value.")
    elif StringVal.lower() == "exit":
        print("To exit, type 'back' and return to the main menu.")
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
    global secon_grade
    print("Welcome to Grade Checker!\n\nPlease choose from the following actions:\nType\n1 - To check grades in scale of 1-100\n2 - To check grades in scale of 1.0-5.0\n3 - To view grades with specified Remarks\nexit - To exit the program")
    TransactionNo = 0
    TransactionLimit = 4
    while True:
        Usr_decision = input("\n> ")
        if Usr_decision == "1":
            print("Type 'back' - To return to the main menu")
            while True:
                init_grade = input("\nEnter Grade: ")
                TransactionNo += 1
                if init_grade.replace(".","").isdecimal() == True:
                    GradeClassifier(Rounder_(init_grade))
                else:
                    if (ValidationResponse(init_grade)) == "return_menu":
                        break
                    else:
                        pass
                if TransactionNo == TransactionLimit:
                    TransactionNo = 0
                    TransactionLimit += 1
                    time.sleep(1)
                    print("\n\nType 'back' - To return to the main menu\nEnter a value - To proceed\n")
                elif TransactionNo > TransactionLimit:
                    TransactionNo = 0
        elif Usr_decision == "2":
            print("Type 'back' - To return to the main menu")
            while True:
                secon_grade = input("\nEnter Grade: ")
                TransactionNo += 1
                if secon_grade.replace(".","").isdecimal() == True:
                    if "." not in secon_grade:
                        UnivGradeClassifier(secon_grade, None)
                    else:
                        Whole, Fraction = secon_grade.split(".")
                        UnivGradeClassifier(Whole[0], Fraction[0:2])
                else:
                    if (ValidationResponse(secon_grade)) == "return_menu":
                        break
                    else:
                        pass
                if TransactionNo == TransactionLimit:
                    TransactionNo = 0
                    TransactionLimit += 1
                    time.sleep(1)
                    print("\n\nType 'back' - To return to the main menu\nEnter a value - To proceed\n")
                elif TransactionNo > TransactionLimit:
                    TransactionNo = 0
        elif Usr_decision == "3":
            print("Type 'back' - To return to the main menu")
            while True:
                tert_grade = input("\nEnter Remarks: ").capitalize()
                TransactionNo += 1
                if tert_grade.lower() == "back":
                    time.sleep(2)
                    print("\n\nWelcome back to the Main Menu!\n\nPlease choose from the following actions:\nType\n1 - To check grades in scale of 1-100\n2 - To check grades in scale of 1.0-5.0\n3 - To view grades with specified Remarks\nexit - To exit the program")
                    break
                elif tert_grade.lower() == "exit":
                    print("To exit, type 'back' and return to the main menu.")
                elif tert_grade.isalpha() == True:
                    RemarksGradeEquival(tert_grade)
                elif tert_grade.isdecimal() == True:
                    print("Input must be a word.")
                elif tert_grade.isalnum() == True:
                    print("Inputs must contain alphabetic characters only.")
                else:
                    print("Please enter a valid input.")
                if TransactionNo == TransactionLimit:
                        TransactionNo = 0
                        TransactionLimit += 1
                        time.sleep(1)
                        print("\n\nType 'back' - To return to the main menu\nEnter a value - To proceed\n")
                elif TransactionNo > TransactionLimit:
                        TransactionNo = 0
        elif Usr_decision.lower() == "exit":
            print("Thank you for stopping by! Have a great day :)")
            break
        else:
            print("Please enter from the menu.")

DecisionMenu()