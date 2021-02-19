class User:

    def __init__(self, first_name, last_name):
        self.firstName=first_name
        self.lastName=last_name
        self.email=input("Enter Email:")
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
        print(f"{self.userName} Login attempts: {self.login_attempts}")

user1=User("Peter","Quill")
user2=User("Gamora","Thanos-Quill")
user3=User("Rocket","Raccoon")

Users=[user1,user2,user3]
for u in Users:
    User.describe_user(u)
    User.greet_user(u)

while user1.login_attempts<5:
    User.login_attempts(user1)
    User.display_attempts(user1)
User.clear_login(user1)
User.display_attempts(user1)
