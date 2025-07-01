family = {
    'father':65,
    'mother':55,
    'children':35
}
print(type(family)) # <class 'dict'>
print(family['mother'])
family['mother'] = 58
family['grandpa'] = 85
family.pop('children')
print(family)