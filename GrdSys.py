import math
def Rounder_(InputGrade):
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
        print("Grade/Mark: 1.0\nDescription: Excellent")
    elif GradeReference >= 94 and GradeReference <= 96:
        print("Grade/Mark: 1.25\nDescription: Excellent")
    elif GradeReference >= 91 and GradeReference <= 93:
        print("Grade/Mark: 1.50\nDescription: Very Good")
    elif GradeReference >= 88 and GradeReference <= 90:
        print("Grade/Mark: 1.75\nDescription: Very Good")
    elif GradeReference >= 85 and GradeReference <= 87:
        print("Grade/Mark: 2.0\nDescription: Good")
    elif GradeReference >= 82 and GradeReference <= 84:
        print("Grade/Mark: 2.25\nDescription: Good")
    elif GradeReference >= 79 and GradeReference <= 81:
        print("Grade/Mark: 2.5\nDescription: Satisfactory")
    elif GradeReference >= 76 and GradeReference <= 78:
        print("Grade/Mark: 2.75\nDescription: Satisfactory")
    elif GradeReference == 75:
        print("Grade/Mark: 3.0\nDescription: Passing")
    elif GradeReference >= 65 and GradeReference <= 74:
        print("Grade/Mark: 5.0\nDescription: Failure")
    else:
        #If-else statements for Inc, Withdrawn, and Dropped
        if GradeReference == "":
            print("")

init_grade = input("Enter Grade: ")
GradeClassifier(Rounder_(init_grade))

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