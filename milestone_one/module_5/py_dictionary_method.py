bio_data={
    'name':'Rakibul Islam',
    'date of birth': "Sep 26, 1991",
    'age': 33,
    'height': '176 cm'
}
# Accessing Elements
print(bio_data['name'])
print(bio_data['date of birth'])
print('The height is',bio_data.get('height'))

#  Update elements
bio_data['age'] = 36
print(bio_data)
bio_data.update({'age':39})
print(bio_data)

# Add Elements
bio_data['alive'] = True
print(bio_data)
bio_data.update({'married':True})
print(bio_data)

# Delete Elements

# del bio_data ['age']
# print(bio_data)
# print(bio_data.clear())
print(bio_data.popitem())
print(bio_data.pop('age'))