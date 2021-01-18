guests=['Spike Cohen', 'Kim Ruff', 'Vermin Supreme']
message=", you are cordially invited to dinner this Saturday."
print("---------------Exercise 3-4------------------")
print(guests[0],message)
print(guests[1],message)
print(guests[2],message)
print("---------------Exercise 3-5------------------")
defer=guests.pop(2)
guests.append("Justin Amash")
message2="will attend."
message3="can not attend. =("
print(guests[0],message2)
print(guests[1],message2)
print(guests[2],message2)
print(defer, message3)
print("---------------Exercise 3-6------------------")
print("OK we are looking to be able to eat at a restaraunt and have bigger tables!")
guests.insert(0, "Bob Marley")
guests.insert(1, "Ludwig von Mises")
guests.insert(5, "Alan Rickman")
for guest in guests:
    print(f"{guest}{message}")
print("---------------Exercise 3-7------------------")
print("Just kidding, restrictions are extended.")
guests2=[guests.pop(5),guests.pop(1),guests.pop(3),guests.pop(0)]
message4=", Sorry I have to retract my invitation."
for guest in guests2:
    print(f"{guest}{message4}")
for guest in guests:
    print(f"{guest}{message}")
print("---------------Exercise 3-9------------------")
print("OK we are looking to be able to eat at a restaraunt and have bigger tables!")
guests.insert(0, "Bob Marley")
guests.insert(1, "Ludwig von Mises")
guests.insert(5, "Alan Rickman")
print(f"I can invite {len(guests)} guests to dinner.")
for guest in guests:
    print(f"{guest}{message}")