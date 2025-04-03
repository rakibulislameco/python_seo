fruits = ['apple','banana', 'orange']
print(type(fruits))
print('Initial List:',fruits)
# Change
fruits[1] = 'cherry'
print('After Change an Element:',fruits)

# Append
fruits.append('Water Melon')
print('After Inserting at last:',fruits)

# Insert
fruits.insert(1,'Pineapple')
print('Insertion:',fruits)

# Extend
numbers = [101,102,103]
numbers_two = [202,204,206]
# numbers.extend(numbers_two)
print(numbers)

# Concate
z = numbers + numbers_two
print(z)

# Removal
fruits.remove('cherry')
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)


