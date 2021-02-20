from user import User
from admin import Admin

class Privileges:
    def __init__(self,privs):
        self.privileges=privs
    
    def display_privileges(self):
        print("The user has these permissions:")
        for p in self.privileges:
            print(p.title()) 
