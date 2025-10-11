class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Vehicle Model: {self.model}, Vehicle Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make, model, year)
        self.body_style = body_style

class ElectricCar(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the electric car...")

tesla = ElectricCar("Tesla", "Cybertruck", "2023", "Triangluar", "125kwh")
tesla.display_info()
print("Body Style:", tesla.body_style)
print("Battery Capacity:", tesla.battery_capacity)
tesla.charge()
