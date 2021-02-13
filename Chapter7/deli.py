sandwich_orders=['Reuben', 'Grilled Cheese', 'BLT', 'Buffalo Chicken']
finished_sandwiches=[]
for s in sandwich_orders:
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)
print(f"Sandwiches made: {finished_sandwiches}")

sandwich_orders=['Reuben', 'Grilled Cheese', 'BLT', 'Buffalo Chicken', "Pastrami", "Pastrami", "Pastrami"]
finished_sandwiches=[]
print("The Deli is out of Pastrami. Sorry.")
for s in sandwich_orders:
    if s != "Pastrami":
        print(f"I made your {s} sandwich.")
        finished_sandwiches.append(s)
    else:
        print(f"I cannot make your {s} sandwich.")
print(f"Sandwiches made: {finished_sandwiches}")