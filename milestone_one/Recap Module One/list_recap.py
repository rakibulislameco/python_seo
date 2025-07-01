fruits = ['apple','banana','orange']
# print(type(fruits))
print(fruits[0])
print('Initial List: ',fruits)
fruits[1] = 'cherry'
print('After change an element: ', fruits)
fruits.append('Water melon')
print('After insertion at last: ', fruits)
fruits.insert(1,'pineapple')
print('Insertion: ', fruits)

numbers = [101, 102, 103]
numbers_two = [202, 204, 206]
# numbers.extend(numbers_two)
print(numbers)

#Concate
z = numbers + numbers_two
print(z)

# removal
fruits.remove('cherry')
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)