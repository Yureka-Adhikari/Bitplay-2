def TwoOddOccuring(arr, size):
    xorof2 = arr[0]
    
    x= 0
    y = 0
    
    setbit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
        
    setbit = xorof2 & ~(xorof2 - 1)
    
    for i in range(size):
        if (arr[i] & setbit):
            x = x^ arr[i]
        else:
            y = y ^ arr[i]
            
    print("The two odd occuring elements are : ", x, "and", y)
    
arr = []

n = int(input("Enter the size of your array : "))

for i in range(n):
    element = int(input("Enter the element : "))
    arr.append(element)
    
TwoOddOccuring(arr, n)