from restaurant import Restaurant
from icecream import IceCreamStand

restaurant1=Restaurant("Red Lobster", "Seafood")
restaurant2=Restaurant("Olive Garden", "Italian")
restaurant3=Restaurant("Agave", "Mexican")
Rs=[restaurant1,restaurant2,restaurant3]

for r in Rs:
    import random
    served=random.randrange(3,26)
    Restaurant.describe_restaurant(r)
    Restaurant.open_restaurant(r)
    Restaurant.number_served(r)
    Restaurant.update_served(r,served)
    Restaurant.number_served(r)

iceCream1=IceCreamStand("Bennies Ice Cream","Dessert")

IceCreamStand.display_flavors(iceCream1)
