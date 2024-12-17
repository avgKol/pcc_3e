import typing


class Battery:
    def __init__(self, battery_size: int):
        if battery_size:
            self.battery_size = battery_size

        else:
            self.battery_size = 40

    def get_range(self):
        if self.battery_size == 40:
            range = 150

        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


battery1 = Battery(50)
print(battery1.battery_size)
battery1.upgrade_battery()
battery1.get_range()
