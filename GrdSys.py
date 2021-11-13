init_grade = int(input("Enter Grade: "))

#Initial Program - Accepts only whole number inputs
if init_grade >= 97 and init_grade <= 100:
    print("Grade/Mark: 1.0\nDescription: Excellent")
elif init_grade >= 94 and init_grade <= 96:
    print("Grade/Mark: 1.25\nDescription: Excellent")
elif init_grade >= 91 and init_grade <= 93:
    print("Grade/Mark: 1.50\nDescription: Very Good")
elif init_grade >= 88 and init_grade <= 90:
    print("Grade/Mark: 1.75\nDescription: Very Good")
elif init_grade >= 85 and init_grade <= 87:
    print("Grade/Mark: 2.0\nDescription: Good")
elif init_grade >= 82 and init_grade <= 84:
    print("Grade/Mark: 2.25\nDescription: Good")
elif init_grade >= 79 and init_grade <= 81:
    print("Grade/Mark: 2.5\nDescription: Satisfactory")
elif init_grade >= 76 and init_grade <= 78:
    print("Grade/Mark: 2.75\nDescription: Satisfactory")
elif init_grade == 75:
    print("Grade/Mark: 3.0\nDescription: Passing")
elif init_grade >= 65 and init_grade <= 74:
    print("Grade/Mark: 5.0\nDescription: Failure")
else:
    #If-else statements for Inc, Withdrawn, and Dropped
    print("")

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