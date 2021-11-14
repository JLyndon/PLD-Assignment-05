age = int(input("Enter age: "))

if (age >= 0) and (age <= 12):
    print("Kid")
else:
    if (age >= 13) and (age <= 17):
        print("Teen")
    else:
        if age == 18:
            print("Debut")
        else:
            if age >= 19:
                print("Adult")
            else:
                print("Enter a valid age.")
                