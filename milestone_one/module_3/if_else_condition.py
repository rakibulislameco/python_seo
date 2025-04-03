number_str = input("Enter Any Number:")
number = int(number_str)

# if number % 2 == 0:
#     print(number, "is even number")
#
# if number % 2 != 0:
#     print(number, "is odd number")

print(number % 2 == 0)
if number % 2 == 0:
    print (number, "is even number")
else:
    print(number, "is odd number")

raining = True

if raining:
    print("take umbrella")
else:
    print("take cap")