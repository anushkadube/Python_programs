#to convert expression
x=input("Enter an expression: ")
operand=""
expression=[]
l=len(x)
for i in range(len(x)):
    if(x[i]>="0" and x[i]<="9"):
        operand+=x[i]
        l-=1
    else:
        expression.append(operand)
        expression.append(x[i])
        operand=""
        l-=1
for i in range(len(x)-l, len(x)):
    operand+=x[i]
expression.append(operand)
#print("Input (in list): ",expression)

"""
#precedence order
order = {"+":3,"-":4,"*":2,"/":1}
print(order)
"""
