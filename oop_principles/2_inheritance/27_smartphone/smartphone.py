class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"Device {self.brand} {self.model} powered on")

    def power_off(self):
        self.is_on = False
        print(f"Device {self.brand} {self.model} powered off")

    def get_info(self):
        return f"Device: {self.brand} {self.model}"


class MobileDevice(Device):
    def __init__(self, brand, model, phone_number, network_type):
        super().__init__(brand, model)
        self.phone_number = phone_number
        self.network_type = network_type

    def get_info(self):
        return f"Device: {self.brand} {self.model} | Mobile: {self.phone_number} ({self.network_type})"

    def connect_to_network(self):
        print(f"Connected to {self.network_type} network")

    def disconnect_from_network(self):
        print(f"Disconnected from {self.network_type} network")


class Battery:
    def __init__(self):
        self.capacity = 4000
        self.current_charge = 85
        self.is_charging = False

    def charge(self):
        self.is_charging = True
        self.current_charge = 100

    def drain(self, amount):
        self.current_charge = max(0, self.current_charge - amount)

    def get_battery_info(self):
        return f"Battery: {self.current_charge}% charged, {self.capacity}mAh capacity"


class Screen:
    def __init__(self):
        self.size = 6.1
        self.resolution = "2532x1170"
        self.brightness = 50
        self.is_cracked = False

    def adjust_brightness(self, level):
        self.brightness = level
        print(f"Screen brightness adjusted to {level}%")

    def crack_screen(self):
        self.is_cracked = True

    def get_screen_info(self):
        return f"Screen: {self.size}in, {self.resolution}, Brightness: {self.brightness}%"


class Camera:
    def __init__(self):
        self.megapixels = 12
        self.has_flash = True
        self.photos_taken = 0

    def take_photo(self):
        self.photos_taken += 1
        print(f"Photo taken! Total photos: {self.photos_taken}, Camera: {self.megapixels}MP")

    def toggle_flash(self):
        self.has_flash = not self.has_flash

    def get_camera_info(self):
        return f"Camera: {self.megapixels}MP, Flash: {self.has_flash}"


class App:
    def __init__(self, name, version, size_mb, category):
        self.name = name
        self.version = version
        self.size_mb = size_mb
        self.category = category

    def launch(self):
        print(f"Launching {self.name}")

    def update(self):
        print(f"Updating {self.name}")

    def get_app_info(self):
        return f"{self.name} v{self.version} - {self.category} ({self.size_mb}MB)"


class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def call(self):
        print(f"Calling {self.name}")

    def send_message(self):
        print(f"Sending message to {self.name}")

    def get_contact_info(self):
        return f"{self.name} - {self.phone_number} ({self.email})"


class Network:
    def __init__(self, name, signal_strength, network_type):
        self.name = name
        self.signal_strength = signal_strength
        self.network_type = network_type

    def broadcast_signal(self):
        print(f"Broadcasting {self.network_type} signal")

    def get_network_info(self):
        return f"{self.name} ({self.network_type}) - Signal: {self.signal_strength}%"


class Smartphone(MobileDevice):
    def __init__(self, brand, model, phone_number, network_type, operating_system, storage_capacity):
        super().__init__(brand, model, phone_number, network_type)
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity
        self.battery = Battery()
        self.screen = Screen()
        self.camera = Camera()
        self.apps = []
        self.contacts = []
        self.network = None

    def get_info(self):
        return f"Device: {self.brand} {self.model} | Mobile: {self.phone_number} ({self.network_type}) | Smartphone: {self.operating_system}, {self.storage_capacity}GB storage"

    def install_app(self, app):
        self.apps.append(app)
        print(f"App {app.name} installed ({app.size_mb}MB)")

    def remove_app(self, app_name):
        self.apps = [a for a in self.apps if a.name != app_name]

    def list_apps(self):
        for app in self.apps:
            print(app.get_app_info())

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added to smartphone")

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def call_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                contact.call()

    def check_battery(self):
        print(self.battery.get_battery_info())

    def adjust_screen(self, level):
        self.screen.adjust_brightness(level)

    def use_camera(self):
        self.camera.take_photo()

    def connect_to_network(self, network=None):
        if network:
            self.network = network
            print(f"Connected to network: {network.name} ({network.network_type}, {network.signal_strength}% signal)")
        else:
            super().connect_to_network()

    def check_signal(self):
        if self.network:
            print(f"Network signal: {self.network.signal_strength}% ({self.network.network_type} - {self.network.name})")
