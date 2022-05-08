print("A python script to find whether the given year is a leap year or not")

yr = int(input("Enter year: "))

if(yr % 400 == 0 and yr % 100 == 0):
    print(yr,"is a leap year")
elif(yr % 100 != 0 and yr % 4 == 0):
    print(yr,"is a leap year")    
else:    
    print(yr,"is not a leap year")
