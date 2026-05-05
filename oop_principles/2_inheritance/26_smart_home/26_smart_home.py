
class PowerMonitor:
    def __init__(self, base_watts):
        self.base_watts    = base_watts
        self.current_watts = 0

    def update_power(self, watts):
        self.current_watts = watts

    def get_usage(self):
        return self.current_watts



class Device:
    def __init__(self, device_id, name, base_watts):
        self.device_id     = device_id
        self.name          = name
        self.is_on         = False
        self.power_monitor = PowerMonitor(base_watts)

    def turn_on(self):
        self.is_on = True
        self.power_monitor.update_power(self.power_monitor.base_watts)

    def turn_off(self):
        self.is_on = False
        self.power_monitor.update_power(0)

    def get_power_usage(self):
        return self.power_monitor.get_usage()

    def get_status(self):
        status = "On" if self.is_on else "Off"
        return f"Device: {self.name} ({self.device_id}) - Status: {status}, Power: {self.get_power_usage()}W"



class Light(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.brightness = 100

    def set_brightness(self, level):
        self.brightness = level

        watts = self.power_monitor.base_watts * (level / 100)
        self.power_monitor.update_power(watts)

    def get_status(self):
        status = "On" if self.is_on else "Off"
        return f"Device: {self.name} ({self.device_id}) - Status: {status}, Brightness: {self.brightness}%, Power: {self.get_power_usage()}W"



class Thermostat(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.temperature = 70.0

    def set_temperature(self, temp):
        self.temperature = temp

    def get_status(self):
        status = "On" if self.is_on else "Off"
        return f"Device: {self.name} ({self.device_id}) - Status: {status}, Temperature: {self.temperature}°F, Power: {self.get_power_usage()}W"



class Camera(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.recording = False

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def get_status(self):
        status    = "On"  if self.is_on    else "Off"
        recording = "Yes" if self.recording else "No"
        return f"Device: {self.name} ({self.device_id}) - Status: {status}, Recording: {recording}, Power: {self.get_power_usage()}W"



class SmartHome:
    def __init__(self, name):
        self.name    = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):
        self.devices = [d for d in self.devices if d.device_id != device_id]

    def get_total_power(self):
        total = 0
        for device in self.devices:
            total = total + device.get_power_usage()
        return total

    def list_devices(self):
        print(f"=== {self.name} Devices ===")
        for device in self.devices:
            print(device.get_status())



living_room_light = Light("L001",      "Living Room Light",  10)
main_thermostat   = Thermostat("T001", "Main Thermostat",    25)
front_camera      = Camera("C001",     "Front Door Camera",   8)

my_home = SmartHome("My Smart Home")
my_home.add_device(living_room_light)
my_home.add_device(main_thermostat)
my_home.add_device(front_camera)

living_room_light.turn_on()
living_room_light.set_brightness(75)

main_thermostat.turn_on()
main_thermostat.set_temperature(68.5)

front_camera.turn_on()
front_camera.start_recording()

my_home.list_devices()
print(f"Total power usage: {my_home.get_total_power()}W")


independent_light = Light("L002", "Bedroom Light", 5)
independent_light.turn_on()
print(f"Independent device power: {independent_light.get_power_usage()}W")

