class Car:
    def __init__(self, brand, model, fuel = 0):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def start_engine(self):
        return print(f"Engine started!")

    def add_fuel(self, amount):
        self.fuel += amount
        return print(f"Fuel: {self.fuel}")

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
        return print(f"Fuel: {self.fuel}")


car1 = Car("Toyota", "Camry")
car1.start_engine()  # Engine started!
car1.add_fuel(10)    # Fuel: 10
car1.drive()         # Fuel: 9