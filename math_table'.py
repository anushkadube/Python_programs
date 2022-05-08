

#for i in range(2, 21, 2):  #table of 2
#    print(i)

#printing table of user defined integer

n = int(input("Enter the number "))
m = n * 10
count = 0
for i in range(n, m+1, n):
    #print(n,"*",i//n, "=",i)
    count = count + 1        
    print("{} * {} = {}".format(n , count, i))
    















