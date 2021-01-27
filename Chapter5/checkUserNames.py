print("=====================5-10=====================")
current_users=['Quill','Gamora','Drax','Rocket','Groot']
new_users=['Gamora', 'Thanos', 'Rocket', 'Thor', 'Vision']
lCurrentUsers=[]
for user in current_users: 
    lCurrentUsers.append(user.lower())
for newUser in new_users:
    if newUser.lower() not in lCurrentUsers:
        print(f"{newUser} is available!")
    else:
        print(f"Sorry, {newUser} has been taken.")