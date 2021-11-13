Numb01 = int(input("Enter first number: "))
Numb02 = int(input("Enter second number: "))
Numb03 = int(input("Enter third number: "))

if (Numb01 < Numb02) and (Numb01 < Numb03):
    print(Numb01)
elif (Numb02 < Numb01) and (Numb02 < Numb03):
    print(Numb02)
elif (Numb03 < Numb01) and (Numb03 < Numb02):
    print(Numb03)

