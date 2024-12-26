from turtle import color
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

language_tuples = ("java", "python", "go", "c", "pascal")
for lang in language_tuples:
    print(f"language is {lang}")

dup_tuples = (1, 2, 3, 2, 1, 4, 5, 2)
print(f"==>> dup_tuples.count(2): {dup_tuples.count(2)}")
print(f"==>> dup_tuples.index(4): {dup_tuples.index(4)}")

countries_tuple = ("USA", "India", "France", "Germany")
if "Canada" in countries_tuple:
    print(f'==>> "yes": {"yes"}')
else:
    print(f'==>> "No": {"No"}')


integer_tuple = (10, 20, 30, 40, 50)
integer_list = list(integer_tuple)
integer_list.append(60)
new_integer_tuple = tuple(integer_list)
print(f"==>> new_integer_tuple: {new_integer_tuple}")

# for number in 1 to 10
squares_tuple = tuple(x**2 for x in range(1, 11))
print(f"==>> squares_tuple: {squares_tuple}")

fruit_list = ["banana", "apple", "pear", "coconut", "papaya"]
print(f"==>> fruit_list[1]: {fruit_list[1]}")
print(f"==>> fruit_list[3]: {fruit_list[3]}")
print(f"==>> fruit_list[-1]: {fruit_list[-1]}")

numbers_list = list(x*10 for x in range(0, 10, 1) if True )
print(f"==>> numbers_list: {numbers_list}")
numbers_list[2]=100
numbers_list.append(60)
numbers_list.remove(40)
print(f"==>> numbers_list: {numbers_list}")

colors_list = ["red", "blue", "green", "yellow", "purple"]
print(f"==>> colors_list[1:3]: {colors_list[1:3]}")
for index in range(0,5):
    print(colors_list[:len(colors_list)-index][::-1])

    
    