#Write a Python program to count the number of even and odd numbers in a list of numbers

numbers = [12, 4545, 54, 156, 12, 11, 2, 14, 11, 13, 156, 111]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f'Total {even} even number and {odd}')