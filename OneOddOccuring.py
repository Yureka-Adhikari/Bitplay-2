def oneoddoccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n = int(input("Enter the size of your array : "))
while (n):
    element = int(input("Enter the element : "))
    arr.append(element)
    n -= 1
    
print("The odd occuring element is : ", oneoddoccuring(arr))