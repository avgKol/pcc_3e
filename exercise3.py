import typing
import collections

fruit_tuple = ("apple", "banana", "pear", "berry", "coconut")
print(type(tuple))
print(tuple[2])

number_tuple = ("10", "20", "30", "40")
# number_tuple[1] = "50"

cities_tuple = ("NYC", "SFO", "ATL")
numbers_tuple = (25, 50, 75)
print(cities_tuple + numbers_tuple)
print(cities_tuple*3)

my_data_tuple = ("Ananta", "43", "Somerset")
# unpack my_data_tuple
name, age, city = my_data_tuple
print(name)
print(age)
print(city)

nested_tuples = (("player1", "50"), ("player2", "75"), ("player3", "100"))
tuple1, tuple2, tuple3 = nested_tuples
player1, score1 = tuple1
player2, score2 = tuple2
player3, score3 = tuple3
print(player1, score1)
print(player2, score2)
print(player3, score3)

for player, score in nested_tuples:
    print(player, score)
