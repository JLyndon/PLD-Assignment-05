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

age = int(input("Enter age: "))
DetermineLifeStage(age)