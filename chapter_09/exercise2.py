import typing


class User:
    def __init__(self, first_name: str, last_name: str, age: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Is Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("John", "Doe", 30, "johndoe@example.com")
user1.describe_user()
user1.greet_user()
user2 = User("Jane", "Doe", 25, "janedoe@example.com")
user3 = User("Bob", "Smith", 40, "bobsmith@example.com")
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)
