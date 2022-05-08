#to reverse a string given by user using a for loop(without swapping)

a = input("Enter a string:")

sum = " "

for i in range(len(a)-1,-1,-1):
    sum += a[i]

print(sum)    


#string reversal using swapping
#strings are immutable        

#a=input("I am Anushka"[::-1])
#print(a)
