def checkifequal(a, b):
    if (a ^ b) != 0:
        print("The two numbers are not equal")
        
    else:
        print("The two numbers are equal")
        
        
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

checkifequal(a, b)