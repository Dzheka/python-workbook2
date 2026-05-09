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
        self.connected = False

    def connect_to_network(self):
        self.connected = True
        print(f"Connected to {self.network_type} network")

    def disconnect_from_network(self):
        self.connected = False
        print("Disconnected from network")

    def get_info(self):
        return f"{super().get_info()} | Mobile: {self.phone_number} ({self.network_type})"


class Smartphone(MobileDevice):
    def __init__(self, brand, model, phone_number, network_type, operating_system, storage_capacity):
        super().__init__(brand, model, phone_number, network_type)
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity

        self.battery = Battery(4000, 85)
        self.screen = Screen(6.1, "1080x2400", 70)
        self.camera = Camera(12, True)

        self.apps = []
        self.contacts = []

        self.network = None

    def get_info(self):
        return (f"{super().get_info()} | Smartphone: {self.operating_system}, "
                f"{self.storage_capacity}GB storage")


    def check_battery(self):
        print(self.battery.get_battery_info())

    def adjust_screen(self, level):
        self.screen.adjust_brightness(level)
        print(f"Screen brightness adjusted to {level}%")

    def use_camera(self):
        self.camera.take_photo()
        print(f"Photo taken! Total photos: {self.camera.photos_taken}, Camera: {self.camera.megapixels}MP")


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
        for c in self.contacts:
            if c.name == name:
                print(c.call())
                return
        print("Contact not found")


    def connect_to_network(self, network=None):
        if network:
            self.network = network
            print(f"Connected to network: {network.name} ({network.network_type}, {network.signal_strength}% signal)")
        else:
            super().connect_to_network()


    def check_signal(self):
        if self.network:
            print(f"Network signal: {self.network.signal_strength}% ({self.network.network_type} - {self.network.name})")
        else:
            print("No network connected")



class Battery:
    def __init__(self, capacity, current_charge):
        self.capacity = capacity
        self.current_charge = current_charge
        self.is_charging = False

    def charge(self):
        self.is_charging = True
        self.current_charge = min(100, self.current_charge + 10)

    def drain(self, amount):
        self.current_charge = max(0, self.current_charge - amount)

    def get_battery_info(self):
        return f"Battery: {self.current_charge}% charged, {self.capacity}mAh capacity"


class Screen:
    def __init__(self, size, resolution, brightness):
        self.size = size
        self.resolution = resolution
        self.brightness = brightness
        self.is_cracked = False

    def adjust_brightness(self, level):
        self.brightness = max(0, min(100, level))

    def crack_screen(self):
        self.is_cracked = True

    def get_screen_info(self):
        return f"Screen: {self.size}\" {self.resolution}, Brightness: {self.brightness}%"


class Camera:
    def __init__(self, megapixels, has_flash):
        self.megapixels = megapixels
        self.has_flash = has_flash
        self.photos_taken = 0

    def take_photo(self):
        self.photos_taken += 1

    def toggle_flash(self):
        self.has_flash = not self.has_flash

    def get_camera_info(self):
        return f"Camera: {self.megapixels}MP, Flash: {'On' if self.has_flash else 'Off'}"



class App:
    def __init__(self, name, version, size_mb, category):
        self.name = name
        self.version = version
        self.size_mb = size_mb
        self.category = category

    def launch(self):
        return f"Launching {self.name}..."

    def update(self):
        return f"{self.name} updated to version {self.version}"

    def get_app_info(self):
        return f"App {self.name} v{self.version} - {self.category} ({self.size_mb}MB)"


class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def call(self):
        return f"Calling {self.name} at {self.phone_number}"

    def send_message(self, message):
        return f"Message to {self.name}: {message}"

    def get_contact_info(self):
        return f"{self.name} - {self.phone_number} ({self.email})"


class Network:
    def __init__(self, name, signal_strength, network_type):
        self.name = name
        self.signal_strength = signal_strength
        self.network_type = network_type

    def broadcast_signal(self):
        return f"Broadcasting {self.network_type} signal at {self.signal_strength}% strength"

    def get_network_info(self):
        return f"{self.name} ({self.network_type}) - Signal: {self.signal_strength}%"
    
# Create independent components (weak composition/aggregation)
contact1 = Contact("Alice", "555-0101", "alice@email.com")
contact2 = Contact("Bob", "555-0102", "bob@email.com")

app1 = App("Instagram", "2.1", 150, "Social")
app2 = App("Calculator", "1.0", 5, "Utility")

network = Network("Verizon", 85, "5G")

# Create smartphone (inheritance + strong composition)
phone = Smartphone("Apple", "iPhone 15", "555-0100", "5G", "iOS 17", 256)

# Test inheritance
phone.power_on()  # From Device
phone.connect_to_network()  # From MobileDevice
print(phone.get_info())  # Overridden in Smartphone

# Test strong composition (integral components)
phone.check_battery()  # Uses internal Battery object
phone.adjust_screen(80)  # Uses internal Screen object
phone.use_camera()  # Uses internal Camera object

# Test weak composition (independent components)
phone.add_contact(contact1)
phone.add_contact(contact2)
phone.install_app(app1)
phone.install_app(app2)

# Test aggregation (shared resource)
phone.connect_to_network(network)
phone.check_signal()

# Demonstrate independence
print(f"Contact exists independently: {contact1.get_contact_info()}")
print(f"App exists independently: {app1.get_app_info()}")
print(f"Network serves multiple devices: {network.get_network_info()}")

# Show what happens when phone is "destroyed"
phone.power_off()
# Battery, Screen, Camera are destroyed with phone (strong composition)
# But Contacts, Apps, and Network continue to exist (weak composition/aggregation)
print(f"Contact still exists: {contact1.name}")
print(f"App still exists: {app1.name}")
print(f"Network still exists: {network.name}")