chickens= {
    'c1': {
        'breed':"Rhode Island Red",
        'age': 'chick',
        'sex': 'hen',
        'price': 1,
        },

    'c2': {
        'breed':"Leghorn",        
        'age': 'adult',
        'sex': 'rooster',
        'price': 20,
        },

    'c3': {
        'breed':"Rhode Island White",        
        'age': 'chick',
        'sex': 'rooster',
        'price': 1.25,
        },

    'c4': {
        'breed':"Guinea",        
        'age': 'adult',
        'sex': 'hen',
        'price': 10,
        },        
}
for chicken, info in chickens.items():
    print(f"\nChicken: {info['breed']}")
    age =info['age']
    sex = info['sex']
    price = info['price']

    print(f"\tAge: {age}")
    print(f"\tSex: {sex}")
    print(f"\tPrice: ${price}")