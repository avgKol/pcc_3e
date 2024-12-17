import typing

class Restaurant:
    def __init__(self, name: str, rating: float, cuisine: str):
        self.name = name
        self.rating = rating
        self.cuisine = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} restaurant with a rating of {self.rating}")
        
    def open_restaurant(self):
        print(f"{self.name} is open!")
    
    def set_number_served(self, number_served: int):
        self.number_served = number_served
        
    def increment_number_served(self, number_served: int):
        self.number_served += number_served

restaurant1 = Restaurant("Papa John's", 4.5, "Pizza")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("Burger King", 4.0, "Burgers")
print(restaurant2.number_served)
restaurant2.number_served = 10
print(restaurant2.number_served)
restaurant2.set_number_served(20)
print(restaurant2.number_served)

class IceCreamStand(Restaurant):
    def __init__(self, name: str, rating: float, cuisine: str, flavors: typing.List[str]):
        super().__init__(name, rating, cuisine)
        self.flavors = flavors

    def display_flavors(self):
        print(f"The flavors are: {self.flavors}")
        
icecreamstand1 = IceCreamStand("Cold Stone", 4.5, "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
icecreamstand1.describe_restaurant()
icecreamstand1.display_flavors()