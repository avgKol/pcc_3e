
dishes = ["pizza", "pasta", "salad", "soup", "steak"]
for dish in dishes:
    print(dish)
    print(f"I love {dish}")

print(f"Do you like food?")

numbers = range(1, 20)
for number in numbers:
    print(number)

even_numbers = range(2, 20, 2)    
for even_number in even_numbers:
    print(even_number)

#This script demonstrates list slicing and iteration by printing favorite activities."""

activities = ["swimming", "running", "cycling", "hiking", "dancing"]

"""This script demonstrates list slicing and iteration over a list of activities."""

# List of favorite activities
activities = ["swimming", "running", "cycling", "hiking", "dancing"]

# Iterate over the first three activities
for activity in activities[:3]:
    print(f"I love {activity}")

# Iterate over activities starting from the third
for activity in activities[2:]:
    print(f"I love {activity}")

# Iterate over activities from the second to the fourth
for activity in activities[1:4]:
    print(f"I love {activity}")

# Iterate over the last three activities
for activity in activities[-3:]:
    print(f"I love {activity}")


fruits = ["apple", "banana", "orange", "grape", "kiwi"]
fruits_2 = fruits.copy()
fruits.append("watermelon")
fruits_2.append("mango")

for fruit in fruits:
    print(fruit)
    print(f"I love {fruit}")

for fruit in fruits_2:
    print(fruit)
    print(f"I love {fruit}")

countries = ("USA", "Canada", "UK", "Germany", "France")
for country in countries:
    print(country)
    print(f"I love {country}")

countries[0] = "Belgium" # This will raise an error because tuples are immutable
