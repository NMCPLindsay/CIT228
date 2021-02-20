from privileges import Privileges
from user import User

class Admin(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        privs=['CanBan','CanModify','CanApprove']
        # self.privileges=['CanModify', 'CanAuthorize', 'CanBan']
        self.privileges=Privileges(privs)

    # def display_privileges(self):
    #     print(f"{self.userName} Privileges: {self.privileges}.")
