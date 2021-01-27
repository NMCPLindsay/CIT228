users=['Quill', 'Gamora', 'Drax', 'Groot','Rocket','admin']
print("=====================5-8======================")
for user in users:
    if user =="admin":
        print("Hello admin, would you like a status report?")
    else:
        print(f"Hello {user}, welcome back.")
print("=====================5-9======================")
users=[]
if users:
    for user in users:
        if user =="admin":
            print("Hello admin, would you like a status report?")
        else:
            print(f"Hello {user}, welcome back.")
else:
    print("We need to find some users.")