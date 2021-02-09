
fred={
   "Name":"Fred",
   "Age":"45",
   "Gender":"Male",
   }
bonnie={
   "Name":"Bonnie",
   "Age":"24",
   "Gender":"Female",
   }
eric={
   "Name":"Eric",
   "Age":"42",
   "Gender":"Male",
   }
employees=[fred,bonnie,eric]
for e in employees:
    print(f"{e['Name']} is a {e['Age']} year old {e['Gender']}.")