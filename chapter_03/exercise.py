names = ["john", "sally", "mark", "lisa", "peter"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"Hello, {names[0]}! You are invited to dinner.")
print(f"Hello, {names[1]}! Have a nice day.")
print(f"Hello, {names[2]}! When are you back from vacation?")
print(f"Hello, {names[3]}! I would like to have cofee with you.")
print(
    f"Hello, {names[4]}! I heard you're moving to Los Angeles. That's great!")

transportation = ["car", "bus", "train", "plane", "boat"]
print(f"I would like to travel by {
      transportation[0]} because it is convenient and fuel-efficient.")
print(f"I often use {
      transportation[1]} to commute to work because it is eco-friendly and cost-effective.")
print(f"I enjoy taking the {
      transportation[2]} for leisurely trips, especially during the fall when the leaves change color.")
print(f"Flying by {
      transportation[3]} is my preferred mode of long-distance travel as it allows me to cover large distances quickly and comfortably.")
print(f"I have also taken a {
      transportation[4]} vacation, which was a relaxing and scenic experience.")

guest_list = ["John", "Sally", "Mark", "Lisa", "Peter"]

guest_list[2] = "James"
print(guest_list)
print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")
print(f"Dear {guest_list[4]}, you are invited to dinner.")


print(f"{guest_list[2]} can't make it to dinner.")
guest_list[2] = "Michael"
print(guest_list)
print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")
print(f"Dear {guest_list[4]}, you are invited to dinner.")
print("I found a bigger dinner table!")

guest_list.insert(0, "Emma")
guest_list.insert(2, "Daniel")
guest_list.append("Olivia")
print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")
print(f"Dear {guest_list[4]}, you are invited to dinner.")
print(f"Dear {guest_list[5]}, you are invited to dinner.")
print(f"Dear {guest_list[6]}, you are invited to dinner.")
print(f"Dear {guest_list[7]}, you are invited to dinner.")

places = ["Paris", "Tokyo", "New York", "Rome", "Sydney"]
print(places)
print(sorted(places))
places.sort(reverse=True)

print(places)

empty_list = []
print(empty_list)
empty_list.append("item1")
empty_list.append("item2")
empty_list.append("item3")
empty_list.append("item4")
empty_list.append("item5")
print(empty_list)
empty_list.pop(2)
print(empty_list)
#Replace the 1st item with a new value.
empty_list[0] = "new item"
print(empty_list)

dishes = ["pizza", "pasta", "salad", "soup", "steak"]
print(len(dishes))


print(dishes[5])
