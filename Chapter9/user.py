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

    def login_attempts(self):
        self.login_attempts+=1
    
    def clear_login(self):
        self.login_attempts = 0

    def display_attempts(self):
        print(f"{self.userName} Login attempts: {self.login_attempts}.")