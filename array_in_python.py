print("In this python script we learnt basic operations of an array")
from array import *    #importing array module
arr = array('i', [1,2,3,4,5])
"""
print("Array : ",arr)
print(arr.buffer_info())
print("Element at index 2 is (here we specified the element) :",arr[2])
print("Element at index 4 is (here we wanted index and specified the element as the parameter) :",arr.index(4))
print("Element at index -2 is :",arr[-2])   #negative index from right to left(-1 to -n)
for i in arr:     #looping through an array
    print(i)
for pnt in range(5):
    #print(arr[pnt])
    print(pnt,arr[pnt])
arr.reverse()          # to reverse the array
print("Reverse array :",arr)
arr.reverse()
arr.append(12)          # to add an element in an array using append 
print("After append :",arr)
arr.extend([13,15,21])          # to add an element in an array using extend
print("After extend :", arr)
arr.insert(3,10)    # to add an element in an array using insert
print("After insert :",arr)

arr.remove(12)    # deleting element using remove(element)
arr.pop(3)        # deleting element using pop(index)
arr.remove(15)
arr.remove(21)
arr.remove(10)
print("Initially array was :",arr)

arr = array('i', [1,2,2,3,4,5])
print("Array is:",arr)
arr.remove(2)
print("Remove '2' from array :",arr)
from array import * 
arr = array('i',[])
#print("Array(empty array) : ",arr)
x  = int(input("Enter size of the array : "))
print("Enter %d elements" %x)
for i in range(x):
    n = int(input())
    arr.append(n)
#print(arr)    

i = 0
while i < x - 1:
    j = i + 1
    while j < x:
        if arr[i] == arr[j]:
             del arr[j]
             x = x - 1
        j += 1
    i += 1
print(arr)    

a = array('d' , [1.1 , 2.1 , 3.1])     # to find the length of an array
print("The lenght of the given array is :", len(a))
b = array('d',[3.2 , 5.1 , 8.1])
c = a + b    # array concatenation
print("After concatenation",c)
"""
print(arr[1:3])         #slicing of an array
print(arr[::-1])




