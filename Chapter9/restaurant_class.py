class Restaurant:
    """ A restaurant """

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine=cuisine
        self.served=0
        

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} restaurant.")
        
    
    def open_restaurant(self):
        print(f"{self.name} is open.")
    
    def number_served(self):
        print(f"Number served: {self.served}")
    
    def update_served(self, n):
        self.served += n 
class IceCreamStand(Restaurant):
    
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors=['Chocolate','Vanilla', 'Strawberry', 'Superman']

    def display_flavors(self):
        print(f"{self.name} flavors include: {self.flavors}")

restaurant1=Restaurant("Red Lobster", "Seafood")
restaurant2=Restaurant("Olive Garden", "Italian")
restaurant3=Restaurant("Agave", "Mexican")
Rs=[restaurant1,restaurant2,restaurant3]

for r in Rs:
    import random
    served=random.randrange(3,26)
    print(Restaurant.describe_restaurant(r))
    print(Restaurant.open_restaurant(r))
    print(Restaurant.number_served(r))
    Restaurant.update_served(r,served)
    print(Restaurant.number_served(r))

iceCream1=IceCreamStand("Bennies Ice Cream","Dessert")

IceCreamStand.display_flavors(iceCream1)