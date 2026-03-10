

class Battery:
    def __init__(self):
        self.charge = 85

    def get_info(self):
        return f"Battery: {self.charge}%"


class Screen:
    def __init__(self):
        self.brightness = 50

    def set_brightness(self, level):
        self.brightness = level
        print(f"Screen brightness: {level}%")


class Camera:
    def __init__(self):
        self.photos = 0

    def take_photo(self):
        self.photos += 1
        print(f"Photo taken! Total: {self.photos}")



class App:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_info(self):
        return f"{self.name} ({self.size}MB)"


class Contact:
    def __init__(self, name, number):
        self.name   = name
        self.number = number

    def call(self):
        print(f"Calling {self.name} at {self.number}")


class Network:
    def __init__(self, name, signal):
        self.name   = name
        self.signal = signal

    def get_info(self):
        return f"{self.name} - {self.signal}% signal"




class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} powered on")

    def power_off(self):
        print(f"{self.brand} {self.model} powered off")


class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand, model)


        self.battery = Battery()
        self.screen  = Screen()
        self.camera  = Camera()


        self.apps     = []
        self.contacts = []
        self.network  = None

    def install_app(self, app):
        self.apps.append(app)
        print(f"App installed: {app.name}")

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added: {contact.name}")

    def connect(self, network):
        self.network = network
        print(f"Connected to {network.name}")

    def check_signal(self):
        if self.network:
            print(self.network.get_info())




app1     = App("Instagram", 150)
app2     = App("Calculator", 5)
contact1 = Contact("Alice", "555-0101")
contact2 = Contact("Bob",   "555-0102")
network  = Network("Verizon", 85)

phone = Smartphone("Apple", "iPhone 15")

phone.power_on()
print()

phone.battery.get_info()
phone.screen.set_brightness(80)
phone.camera.take_photo()
print()

phone.install_app(app1)
phone.install_app(app2)
phone.add_contact(contact1)
phone.add_contact(contact2)
print()

phone.connect(network)
phone.check_signal()
print()

phone.power_off()
print(f"Contact still exists: {contact1.name}")
print(f"App still exists:     {app1.name}")
print(f"Network still exists: {network.name}")
