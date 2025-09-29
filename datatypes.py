number = int(input("Enter the number: "))

if(number % 2 == 0):
    print("yes its an even number.")
else:
    print("its an odd number")


#find grater of 3 numbers

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
num3 = int(input("Enter 3st number: "))

if(num1 > num2 and num1 > num3):
    print("num1 is the greater")
elif(num2 > num3 and num2 > num1):
    print("2nd is grater")

else:
    print("3rd no is greater")


#check if a number is a multiple of 7\

num = int (input("Enter the number for cheking multiple of 7:"))

if(num % 7 == 0):
    print("yes its a multiple of 7")
else:
    print("not a multiple of 7.")


