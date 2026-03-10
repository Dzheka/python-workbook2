class PowerMonitor:
    def __init__(self, base_watts):
        self.base_watts = base_watts
        self.current_watts = base_watts

    def update_power(self, watts):
        self.current_watts = watts

    def get_usage(self):
        return self.current_watts


class Device:
    def __init__(self, device_id, name, base_watts):
        self.device_id = device_id
        self.name = name
        self.is_on = False
        self.power_monitor = PowerMonitor(base_watts)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_status(self):
        return f"Device: {self.name} ({self.device_id}) - Status: {'On' if self.is_on else 'Off'}"

    def get_power_usage(self):
        return self.power_monitor.get_usage() if self.is_on else 0


class Light(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.brightness = 100

    def set_brightness(self, level):
        self.brightness = level
        self.power_monitor.update_power(self.power_monitor.base_watts * level / 100)


class Thermostat(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.temperature = 70.0

    def set_temperature(self, temp):
        self.temperature = temp


class Camera(Device):
    def __init__(self, device_id, name, base_watts):
        super().__init__(device_id, name, base_watts)
        self.recording = False

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False


class SmartHome:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):
        self.devices = [d for d in self.devices if d.device_id != device_id]

    def get_total_power(self):
        return sum(d.get_power_usage() for d in self.devices)

    def list_devices(self):
        print(f"=== {self.name} Devices ===")
        for device in self.devices:
            print(device.get_status())
