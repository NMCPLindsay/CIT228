print("=============7-2===============")

party=input("How many people are in your party?")

if int(party)>8:
    print("We apologize, but you will have to wait for a table.")
else:
    print(f"{party}? Your table is ready.")
