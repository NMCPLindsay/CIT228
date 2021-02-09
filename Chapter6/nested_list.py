eric={
   "Name":"Eric",
   "Age":"42",
   "Gender":"Male",
   "favFoods":["Shrimp","Tilapia","Tacos Pastor"]
   }
print(f"{eric['Name']} likes to eat:")
for key, value in eric.items():
    if type(value)==list:
        for v in value:
            print("\t\t\t",v)