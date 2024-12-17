import typing


def display_message():
    """Prints a simple message."""
    print("I'm learning about functions in this chapter.")


def favorite_book(title):
    """Prints a message about a favorite book."""
    print(f"One of my favorite books is {title}.")


def make_shirt(size, message):
    """Prints a message about the shirt size and message."""
    print(f"The shirt size is {size} and the message is {message}.")


def describe_city(city, country="USA"):
    """Prints a message about a city and its country."""
    print(f"{city} is in {country}.")


def city_country(city, country):
    """Returns a string with the city and country."""
    return f"{city}, {country}"


def make_album(artist, title, tracks=None):
    """Returns a dictionary with the artist and title."""
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album


def show_messages(messages):
    """Prints each message in a list."""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Prints each message in a list and moves it to a new list."""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


def sandwich(*items):
    """Prints a summary of the sandwich being ordered."""
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


def make_car(manufacturer: str, model: str, **kwargs) -> typing.Dict[str, typing.Any]:
    """Build a dictionary containing everything we know about a car."""
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs


# Only execute these when the file is run directly, not when imported
if __name__ == "__main__":
    display_message()
    favorite_book("Alice in Wonderland")
    make_shirt("M", "I love Python!")
    describe_city("New York")
    describe_city("Los Angeles")
    describe_city("Paris", "France")
    print(city_country("Santiago", "Chile"))
    print(city_country("Paris", "France"))
    print(city_country("Tokyo", "Japan"))
    print(make_album("The Beatles", "Abbey Road"))
    print(make_album("Pink Floyd", "The Wall"))
    print(make_album("Led Zeppelin", "Led Zeppelin IV", 8))
    print(make_album("The Rolling Stones", "Exile on Main St."))

    messages = ["Hello", "How are you?", "I'm fine."]
    show_messages(messages)

    messages = ["Hello", "How are you?", "I'm fine."]
    sent_messages = []
    send_messages(messages, sent_messages)
    print(sent_messages)

    sandwich("ham", "cheese", "lettuce", "tomato")
    sandwich("turkey", "bacon", "avocado")
    sandwich("peanut butter", "jelly")

    car = make_car("subaru", "outback", color="blue", tow_package=True)
    print(car)
