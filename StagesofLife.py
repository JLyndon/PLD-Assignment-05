def DetermineLifeStage(Usr_Age):
    if (Usr_Age >= 0) and (Usr_Age <= 12):
        print("Kid")
    else:
        if (Usr_Age >= 13) and (Usr_Age <= 17):
            print("Teen")
        else:
            if Usr_Age == 18:
                print("Debut")
            else:
                if Usr_Age >= 19:
                    print("Adult")
                else:
                    print("Enter a valid age.")

while True:
    age = input("\nEnter age: ")
    if age.isalpha() == True:
        print("Input must be a number.")
    elif age.isdecimal() == True:
        ConventionalAge = int(age)
        DetermineLifeStage(ConventionalAge)
        break
    elif "." in age:
        if age.replace(".","").isdecimal() == True:
            DecimalAge = float(age)
            DetermineLifeStage(DecimalAge)
            break
    elif age.isalnum() == True:
        print("Input must only consist of numbers.")
    else:
        print("Please enter a valid age.")
