from restaurant import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors=['Chocolate','Vanilla', 'Strawberry', 'Superman']

    def display_flavors(self):
        print(f"{self.name} flavors include: {self.flavors}")