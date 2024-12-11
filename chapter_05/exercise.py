favorite_color = "red"
if favorite_color == "blue":
    print("My favorite color is blue")
else:
    print("My favorite color is red")

age = 20
if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")

fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("You really like apples!")
if "banana" in fruits:
    print("You really like bananas!")
if "cherry" in fruits:
    print("You really like cherries!")


current_users = ["admin", "user1", "user2", "user3", "user4"]
new_users = ["user1", "user5", "user6", "admin", "user7"]
for new_user in new_users:
    if new_user in current_users:
        print(f"You will need to enter a new username, {new_user} is taken")
    else:
        print(f"The username {new_user} is available")

temperature = 40
humidity = 65
if temperature > 40 and humidity > 60:
    print("It's too hot and humid outside")
elif temperature > 40 or humidity > 60:
    print("It's either too hot or too humid outside")
else:
    print("It's neither too hot nor too humid outside")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")