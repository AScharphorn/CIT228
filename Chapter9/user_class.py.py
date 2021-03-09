attempt=""
class User:
    def __init__(self, first_name, last_name, username, password, email, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.login_attempts = 0

    def describer_user(self):
        print(f"{self.first_name} {self.last_name} has a username of {self.username},")
        print(f"and has a password of {self.password} with an email address of {self.email}")

    def greet_user(self):
        print(f"Welcome back {self.first_name}!")

    def increment_login_attempts(self):
        if attempt!=self.password:
            self.login_attempts += 1
    
    def reset_login_attempts(self):
        if self.login_attempts==5:
            self.login_attempts==0

user1 = User("Steven","Price","stevenprice","password1","steven@price.net",0)
user2 = User("Cynthia","Rogers","cynthiarogers","zypher","cynthia@rogers.net",0)
user3 = User("Virgil","Carter","virgilcarter","sports","virgil@carter.net",0)

while user1.login_attempts<5 and attempt!=user1.password:
    print(f"{user1.first_name} has tried to login {user1.login_attempts} times.")
    #password is password1
    attempt=input("Password: ")
    user1.increment_login_attempts()
    if attempt==user1.password:
        user1.greet_user()
        user1.describer_user()
        print()
        user2.greet_user()
        user2.describer_user()
        print()
        user3.greet_user()
        user3.describer_user()
if user1.login_attempts==5:
    print(f"Sorry {user1.first_name} but you have failed to login after {user1.login_attempts} attempts and your account has been locked for 30 minutes.")
    user1.reset_login_attempts()