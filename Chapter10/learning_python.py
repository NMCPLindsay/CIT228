filename="Chapter10/learning_python.txt"

with open(filename) as pyfile:
    learning=pyfile.read()
print(learning)

with open(filename) as pyfile:
    for line in pyfile:
        print(line)

with open(filename) as pyfile:
    learning=pyfile.readlines()
print("Original List: ", learning)

for line in learning:
    print(line)

with open(filename) as pyfile:
    print("Original List: ")
    for line in pyfile:
        print(line)
    
with open(filename) as pyfile:
    print("Modified List: ")
    for line in pyfile:
        print(line.replace("python","C#"))
