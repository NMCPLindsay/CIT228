class User:

    def __init__(self, first_name, last_name):
        self.firstName=first_name
        self.lastName=last_name
        # self.email=input("Enter Email:")
        self.userName=input("Enter Username:")
        self.login_attempts=0
    
    def describe_user(self):
        print(f"""Username: {self.userName}\n Name: {self.firstName.title()} {self.lastName.title()}\n Email: {self.email}""")
    
    def greet_user(self):
        print(f"Hello, {self.userName}.")

    def login_attempt(self):
        self.login_attempts+=1
    
    def clear_login(self):
        self.login_attempts = 0

    def display_attempts(self):
        print(f"{self.userName} Login attempts: {self.login_attempts}.")
        
class Admin(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        privs=['CanBan','CanModify','CanApprove']
        # self.privileges=['CanModify', 'CanAuthorize', 'CanBan']
        self.privileges=Privileges(privs)

    # def display_privileges(self):
    #     print(f"{self.userName} Privileges: {self.privileges}.")

class Privileges:
    def __init__(self,privs):
        self.privileges=privs
    
    def display_privileges(self):
        print("The user has these permissions:")
        for p in self.privileges:
            print(p.title())    

user1=Admin("Peter","Quill")

Privileges.display_privileges(user1)
