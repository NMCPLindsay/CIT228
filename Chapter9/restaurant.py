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