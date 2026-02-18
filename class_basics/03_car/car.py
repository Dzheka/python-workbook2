class Car():
    def __init__(self,brand,model,fuel = 0) ->None:
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def start_engine(self):
        print("Engine started!")

    def add_fuel(self,amount):
        total = self.fuel+amount
        print(f"Fuel: {total}")

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
        print(f"Fuel: {self.fuel}")

car1 = Car("Toyota", "Camry")
car1.start_engine()
car1.add_fuel(10)
car1.drive()
