# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# 1 +4 +7 +10 +13 ...........
# sum = 0
# sum = sum +1 = 1
# sum = sum +2 = 3
# sum = sum +3 = 6
# sum = sum +4 = 10

sum = 0
number = 1
last_number = int(input("The Number is : "))
# while number <= 10:
while number <= last_number:
    print('Number value is', number)
    sum = sum + number
    # number = number + 1
    number = number + 3
    print ('sum value', sum)

print(f'The sum of number is {sum}')

