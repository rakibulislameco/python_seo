family = {
'father': 65,
'mother': 55,
'children':35
}

# print(type(family))
print(family ['mother']) #55
family['mother'] = 58
family['grandpa'] = 85
family.pop('children')
family.update({'mother':90})
print(family)
print(family.get('father'))