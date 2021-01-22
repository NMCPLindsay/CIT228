print("------------------4-8---------------")
numbers=list(range(10))
for n in numbers:
    print((n+1)**3)
    
print("------------------4-9---------------")
cubes=[(n+1)**3 for n in numbers]
print(cubes)
