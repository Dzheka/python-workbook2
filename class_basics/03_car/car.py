class Car:
    def init(self, brand, model):
        self.brand = brand
        self.model = model
        self.fuel = 0

    def start_engine(self):
        print("Engine started!")

    def add_fuel(self, amount):
        self.fuel += amount
        print(f"Fuel: {self.fuel}")

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"Fuel: {self.fuel}")
        else:
            print("Not enough fuel!")
