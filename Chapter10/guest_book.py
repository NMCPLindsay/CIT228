
# with open("Chapter10/guests.txt","a") as guestFile:
#     name=input("What is your name?")
#     guestFile.write(name)

# with open("Chapter10/guests.txt","w") as guestFile:
#     counter=0
#     while counter<5:        
#         name=input("What is your name?")
#         guestFile.write(name)
#         guestFile.write("\n")
#         print(f"Welcome, {name}")
#         counter+=1
import os
import random

filename="Chapter10/guests.txt"

if os.path.exists(filename):
    os.remove(filename)

rooms=[]
with open(filename,"w") as guestFile:
    guest=input("Enter your name or enter 'q' to quit: ")
    while guest != 'q':
        number=random.randint(1,25)
        while number in rooms:
            number=random.randint(1,25)
        print(f"{guest} is assigned to room {number}.")
        rooms.append(number)
        guest+=", Room:"+ str(number) + "\n"
        guestFile.write(guest)
        guest=input("Enter your name or enter 'q' to quit: ")
with open(filename) as guestFile:
    print("==================Guest and Room Assigned================\n")
    for line in guestFile:
        print(line)
