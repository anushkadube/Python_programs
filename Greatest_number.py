#Wap to find the greatest number between 3 numbers, also take the input from user

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

a = int(a)
b = int(b)
c = int(c)

if(a == b == c):
    print("All values are same")
    
elif(a == b > c):
    print(a,"and" , b, "are equal.", c, "is smaller than both. ")
elif(c == b > a):
    print(c,"and" , b, "are equal.", a, "is smaller than both. ")
elif(a == c > b):
    print(a,"and" , c, "are equal.", b, "is smaller than both. ")
    
elif(a == b < c):
    print(a,"and" , b, "are equal.", c, "is greater than both. ")
elif(a == c < b):
    print(a,"and" , c, "are equal.", b, "is greater than both. ")
elif(c == b < a):
    print(c,"and" , b, "are equal.", a, "is greater than both. ")

    
elif(a>b and a>c):
    print(a, "is greater than ",b, "and ", c)
elif(b>a and b>c):
    print(b , "is greater than ", a ,"and ", c)
else:
    print(c, "is greater than ", a , "and " , b)
    
