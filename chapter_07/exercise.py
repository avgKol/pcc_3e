# Write a program that asks the user what kind of rental car they would like.
# Print a message about that car, such as "Let me see if I can find you a Subaru."
from itertools import count


car = input("What kind of rental car would you like? ")
print("Let me see if I can find you a " + car.title() + ".")
# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying they’ll have to wait for a table.
# Otherwise, report that their table is ready.
group = input("How many people are in your dinner group? ")
group = int(group)
if group > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
# Write a program that asks the user for a number and then reports whether the number is a multiple of 10 or not.
number = input("Give me a number: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
# Write a loop that prompts the user to enter a series of pizza toppings until they type 'quit'.As they enter each topping, print a message saying you’ll add that topping to their pizza.
prompt = "What topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
while True:
    topping = input(prompt)
    if topping != "quit":
        print("  I'll add " + topping + " to your pizza.")
    else:
        break
# Write a program that asks the user for their age and calculates the cost of their movie ticket: Free for ages under 3. $10 for ages 3–12. $15 for ages 13 and above.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
while True:
    age = input(prompt)
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("  You're free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")

# Create an infinite loop and observe its behavior.
counter = count(start=1)
while True:
    print("Hello World!" + str(next(counter)))
