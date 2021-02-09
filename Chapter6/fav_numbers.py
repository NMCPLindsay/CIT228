print("=================6-2==================")
Frank={'Number': 5, 'Name': 'Frank'}
Fred={'Number': 4, 'Name': 'Fred'}
Tom={'Number':3, 'Name': 'Tom'}
Vi={'Number':2, 'Name': 'Vi'}
O={'Number':1, 'Name': 'O'}
List=[Frank,Fred,Tom,Vi,O]

for a in List:
    print(f"{a['Name']}'s number is {a['Number']}.")