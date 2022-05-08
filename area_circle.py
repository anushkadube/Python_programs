#finding area of circle and rounding off the area

rad = int(input("Enter the radius of the circle: "))

area = 3.14 * rad * rad
print("The area of circle:",area)

#using round of function round(variable to be round off, number of places after decimals)

area = round(area,3)
print("The area of circle after rounding-off:",area)
