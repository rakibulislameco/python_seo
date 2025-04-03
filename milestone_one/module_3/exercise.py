# a = int(input("Enter first number: "))
# b = int(input("Enter second number"))
#
# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("a is less than b")
from operator import truediv

# completed = False
# if completed:
#     print("https://www.celebheights.com/")
# else:
#     print("I didn't see that site")

name = input("Enter Celebrity Name: ")
height = float(input("Enter height in CM "))
height_m = round(height/ 100, 2)
height_inches = round(height/ 2.54, 2)

height_feet = height_inches // 12
remaining_inches = height % 12
print(name+"'s Height")
print("height " + str(height) +"CM")
print("height_m " + str(height_m) +"M")
print("height_inches " + str(height_inches) +"M")
print(height_feet, 'feet', remaining_inches, "inches")