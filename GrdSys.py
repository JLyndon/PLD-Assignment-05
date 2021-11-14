import math
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
        return print(f"The rating is unavailable for the grade {GradeReference}.")

def DecisionMenu():
    print("Welcome to Grade Checker!\n\nPlease choose from the following actions:\nType\n1 - To check grades in scale of 1-100\n2 - To check grades in scale of 1.0-5.0\n3 - To view grades with specified Remarks\nexit - To exit the program")
    while True:
        Usr_decision = input("\n> ")
        if Usr_decision == "1":
            print("Type 'back' - To return to the main menu")
            while True:
                init_grade = input("\nEnter Grade: ")
                if init_grade.replace(".","").isdecimal() == True:
                    GradeClassifier(Rounder_(init_grade))
                elif init_grade.isalpha() == True:
                    print("Please enter a numeric grade.")
                elif init_grade.isalnum() == True:
                    print("Inputs must be numbers only.")
                else:
                    print("Please enter a valid input.")
        elif Usr_decision == "2":
            init_grade = input("Enter Grade: ")
        elif Usr_decision == "3":
            init_grade = input("Enter Grade: ")
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