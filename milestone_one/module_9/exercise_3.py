# Write a Python program to convert temperatures to and from Celsius and Fahrenheit

temp = input("Enter Temperature 10F, 30C: ")
degree = int(temp[:-1])
unit = temp[-1]

if unit.upper() == 'C':
    # print('Celsius Calculation')
    result = degree * 1.8 + 32
    unit = 'Farenheit'
elif unit.upper() == 'F':
    # print('Farenheit Calculation')
    result = (degree - 32) * (5/9)
    unit = 'Celsius'
else:
    print('Enter Proper Unit')
    quit()
print(f'you have input{temp} in {result} {unit}')