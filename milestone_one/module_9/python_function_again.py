# def greetings(first_name, last_name):
#     msg = f'Howdy {first_name},{last_name}'
#     return msg
#
# greet1 = greetings('Rakibul','Islam')
# print(greet1)

# def add(a,b):
#     sum = a + b
#     return sum
# first = add(5,6)
# print (first)

# Salman khan is a actor. He is 56 years old

def bio(name, sex, age):
    if sex.lower() == "male":
        pronoun = "He"
    else:
        pronoun = "She"
    sentence = f'{name} is an actor. {pronoun} is {age} years old'
    return sentence

# srk = bio('Sharuk khan', 'male', "45")
# print (srk)
katrina = bio('Katrina', 'female', "60")
print (katrina)


