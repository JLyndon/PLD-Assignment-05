Numb01 = int(input("Enter first number: "))
Numb02 = int(input("Enter second number: "))
Numb03 = int(input("Enter third number: "))

#Accepts inputs only with unique values
if (Numb01 < Numb02) and (Numb01 < Numb03):
    print(Numb01)
elif (Numb02 < Numb01) and (Numb02 < Numb03):
    print(Numb02)
elif (Numb03 < Numb01) and (Numb03 < Numb02):
    print(Numb03)
elif (Numb03 == Numb01) and (Numb03 == Numb02):
    print(Numb01)
else: #Accepts inputs with alike values and still solve for the lowest value
    if (Numb01 == Numb02) or (Numb01 == Numb03):
        print(Numb01)
    elif (Numb02 == Numb01) or (Numb02 == Numb03):
        print(Numb02)
    elif (Numb03 == Numb01) or (Numb03 == Numb02):
        print(Numb03)