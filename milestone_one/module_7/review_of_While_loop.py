# i = 1
# number = 1
# # while i <= 10:
# while True:
#     print('The current value of i is', number)
#     # i += 1
#     number = number +1
#---------****************-------------

# 10,54151,24514,541545,64545,454545,4545,48545,45,5454,545

sum = 0

while True:
    user_input = input("Enter a number or t to terminate: ")
    if user_input == 't':
        break
    sum = sum + int(user_input)
print('The total amount is', sum)