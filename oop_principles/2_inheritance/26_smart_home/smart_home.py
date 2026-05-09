class PowerMonitor:
    def __init__(self, base_watts):
        self.base_watts = base_watts
        self.current_watts = 0.0

    def update_power(self, watts):
        self.current_watts = watts
    
    def get_usage(self):
        return self.current_watts
    
class Device:
    def __init__(self, device_id, name, base_watts):
        self.device_id = device_id
        self.name = name
        self.power_monitor = PowerMonitor(base_watts)
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        self.power_monitor.update_power(self.power_monitor.base_watts)
    
    def turn_off(self):
        self.is_on = False
        self.power_monitor.update_power(0.0)
    
    def get_status(self):
        return f"Device: {self.name} ({self.device_id}) - Status: {'on' if self.is_on else 'Off'}"
    
    def get_power_usage(self):
        return self.power_monitor.get_usage()
    
class Light(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.brightness = 0

    def set_brightness(self, level):
        if self.is_on:
            self.brightness = max(0, min(100, level))

class Thermostat(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.temperature = None

    def set_temperature(self, temp):
        if self.is_on:
            self.temperature = temp
            self.power_monitor.update_power(self.power_monitor.base_watts)
    
    def get_status(self):
        return (f"Device: {self.name} ({self.device_id}) - Status: {'On' if self.is_on else 'Off'}, "
                f"Temperature: {self.temperature}°F, Power: {self.get_power_usage():.1f}W")


class Camera(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.recording = False

    def start_recording(self):
        if self.is_on:
            self.recording = True
            self.power_monitor.update_power(self.power_monitor.base_watts)

    def stop_recording(self):
        self.recording = False
        if self.is_on:
            self.power_monitor.update_power(self.power_monitor.base_watts)
    
    def get_status(self):
        return (f"Device: {self.name} ({self.device_id}) - Status: {'On' if self.is_on else 'Off'}, "
                f"Recording: {'Yes' if self.recording else 'No'}, Power: {self.get_power_usage():.1f}W")


class SmartHome:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):
        self.devices = [d for d in self.devices if d.devices != device_id]

    def get_total_power(self):
        return sum(d.get_power_usage() for d in self.devices)

    def list_devices(self):
        print(f"==={self.name} Devices===")
        for d in self.devices:
            print(d.get_status())

# Create devices (each device HAS-A PowerMonitor - composition)
living_room_light = Light("L001", "Living Room Light", 10)
main_thermostat = Thermostat("T001", "Main Thermostat", 25)
front_camera = Camera("C001", "Front Door Camera", 8)

# Create smart home system (aggregation)
my_home = SmartHome("My Smart Home")

# Add devices to home system (aggregation - devices can exist independently)
my_home.add_device(living_room_light)
my_home.add_device(main_thermostat)
my_home.add_device(front_camera)

# Control individual devices
living_room_light.turn_on()
living_room_light.set_brightness(75)

main_thermostat.turn_on()
main_thermostat.set_temperature(68.5)

front_camera.turn_on()
front_camera.start_recording()

# Display home status
my_home.list_devices()
print(f"Total power usage: {my_home.get_total_power()}W")

# Demonstrate aggregation - device can exist independently
independent_light = Light("L002", "Bedroom Light", 5)
independent_light.turn_on()
print(f"Independent device power: {independent_light.get_power_usage()}W")