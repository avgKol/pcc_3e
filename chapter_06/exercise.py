import aliens


user = {"name": "John", "age": 30, "city": "New York", "email": "john@example.com"}
for key, value in user.items():
    print(f"{key}: {value}")

name_numbers = {"John": 30, "Alice": 25, "Bob": 35, "Eve": 28}
for name, number in name_numbers.items():
    print(f"{name}: {number}")

programmingterm_defintion = {
    "variable": "A container for storing data values.",
    "function": "A block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code multiple times.",
    "conditional statement": "A control structure that executes different code based on a condition.",
}
for term, definition in programmingterm_defintion.items():
    print(f"{term}: {definition}")

river_country = {"Nile": "Egypt", "Amazon": "Brazil", "Yangtze": "China"}
for river, country in river_country.items():
    print(f"The {river} River runs through {country}.")

for river in river_country.keys():
    print(river)

for country in river_country.values():
    print(country)

favorite_languages = {
    "John": "Python",
    "Alice": "JavaScript",
    "Bob": "Java",
    "Eve": "Python",
}
names = ["John", "Alice", "Bob", "Eve", "Frank"]
for name in names:
    if name in favorite_languages:
        print(f"Thank you for taking the poll, {name}!")
    else:
        print(f"Please take our poll, {name}!")

pets = {
    "pet1": {"type": "dog", "owner": "John"},
    "pet2": {"type": "cat", "owner": "Alice"},
    "pet3": {"type": "fish", "owner": "Bob"},
}

for pet_id, pet_info in pets.items():
    print(f"\nPet ID: {pet_id}")
    for key in pet_info:
        print(f"{key}: {pet_info[key]}")

cities = {
    "New York": {
        "country": "USA",
        "population": 8_400_000,
        "fact": "The Empire State Building is the tallest building in the world.",
    },
    "London": {
        "country": "UK",
        "population": 9_000_000,
        "fact": "London has a Queen's University.",
    },
    "Paris": {
        "country": "France",
        "population": 2_100_000,
        "fact": "Paris is known for its art and culture.",
    },
}
for city, city_info in cities.items():
    print(f"\nCity: {city}")
    for key in city_info:
        print(f"{key}: {city_info[key]}")

aliens = [
    {"color": "green", "points": 5, "speed": "slow"},
    {"color": "yellow", "points": 10, "speed": "medium"},
    {"color": "red", "points": 15, "speed": "fast"},
]

# Modify some aliens in the list (e.g., change their color and speed) and print the updated list.
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"

for alien in aliens[:5]:
    print(alien)

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

for language in set(favorite_languages.values()):
    print(language)
