print("This script is intended to swap the values of two data variables using a third temporary variable\n")

a = input("Enter first number:")
b = input("Enter second number:")

print("Before swapping numbers are :",a,b)
"""
a = int(a)    you can skip these two steps
b = int(b)
"""
temp = a
a = b
b = temp

print("After swapping of two numbers first number is",a,"and second number is",b )
"""
II a = a+b
   b = a-b
   a = a-b
III a,b = b,a (in python)

"""
