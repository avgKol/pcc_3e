import exercise_1
from exercise_1 import make_car as manufacture_car

car1 = manufacture_car("subaru", "outback", motor="v8", year=2019)
print(car1)
car2 = manufacture_car("subaru", "outback", color="blue", motor="v6", year=2019)
print(car2)
car3 = manufacture_car("subaru", "outback", color="blue", motor="v6", year=2019)
print(car3)
