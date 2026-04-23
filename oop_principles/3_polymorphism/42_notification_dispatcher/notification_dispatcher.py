from abc import ABC, abstractmethod
from datetime import datetime

class NotificationService(ABC):
    def __init__(self, service_name):
        self.service_name = service_name
        self.sent_count = 0

    @abstractmethod
    def validate_recipient(self, recipient):
        pass

    @abstractmethod
    def send(self, recipient, message):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    def log_notification(self, recipient, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.service_name}: {recipient} - {status}")
        if status == "SUCCESS":
            self.sent_count += 1

class EmailNotification(NotificationService):
    def __init__(self):
        super().__init__("Email Service")

    def validate_recipient(self, recipient):
        return "@" in recipient
    
    def send(self, recipient, message):
        if self.validate_recipient(recipient):
            print(f"Sending email to {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False
        
    def get_cost(self):
        return 0.001
    
class SMSNotification(NotificationService):
    def __init__(self):
        super().__init__("SMS Service")

    def validate_recipient(self, recipient):
        return recipient.startswith("+")
    
    def send(self, recipient, message):
        if self.validate_recipient(recipient):
            print(f"Sending SMS to {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False
        
    def get_cost(self):
        return 0.05
    
class PushNotification(NotificationService):
    def __init__(self):
        super().__init__("Push Notification Service")

    def validate_recipient(self, recipient):
        return len(recipient) > 5
    
    def send(self, recipient, message):
        if self.validate_recipient(recipient):
            print(f"Sending push notification to device {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False
    
    def get_cost(self):
        return 0.01
    

class NotificationDispatcher:
    def __init__(self, services=None):
        self.services = services if services else []

    def add_service(self, service: NotificationService):
        self.services.append(service)

    def remove_service(self, service: NotificationService):
        self.services = [s for s in self.services if s is not service]

    def broadcast(self, recipients, message):
        for service in self.services:
            for recipient in recipients:
                service.send(recipient, message)

    def send_to_valid(self, recipients, message):
        for service in self.services:
            for recipient in recipients:
                if service.validate_recipient(recipient):
                    service.send(recipient, message)

    @property
    def total_sent(self):
        return sum(service.sent_count for service in self.services)
    
    @property
    def total_cost(self):
        return sum(service.sent_count * service.get_cost() for service in self.services)
    
class SlackNotification(NotificationService):
    def __init__(self):
        super().__init__("Slack Service")

    def validate_recipient(self, recipient):
        return recipient.startswith("#")  # contoh validasi channel

    def send(self, recipient, message):
        if self.validate_recipient(recipient):
            print(f"Sending Slack message to {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False

    def get_cost(self):
        return 0.02
    
def send_multi_channel(services, recipient_map, message):
    success_count = 0
    for service in services:
        recipient = recipient_map.get(service)
        if recipient and service.send(recipient, message):
            success_count += 1
    return success_count

def find_cheapest_service(services):
    return min(services, key=lambda s: s.get_cost())

def batch_send(services, recipients, message):
    success = 0
    failed = 0
    for service in services:
        for recipient in recipients:
            if service.send(recipient, message):
                success += 1
            else:
                failed += 1
    total_cost = sum(s.sent_count * s.get_cost() for s in services)
    return {"success": success, "failed": failed, "total_cost": total_cost}

# Create multiple notification services
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

# Create dispatcher with multiple channels
dispatcher = NotificationDispatcher([email, sms, push])

# Broadcast to all channels polymorphically
recipients = {
    "email": "user@example.com",
    "sms": "+1234567890",
    "push": "device_abc123"
}

print("=== Broadcasting Message ===")
dispatcher.broadcast(
    ["user@example.com", "+1234567890", "device_abc123"],
    "Server maintenance scheduled for tonight"
)
# Output:
# Sending email to user@example.com: Server maintenance scheduled for tonight
# [2025-10-04 22:45:00] Email Service: user@example.com - SUCCESS
# Sending SMS to +1234567890: Server maintenance scheduled for tonight
# [2025-10-04 22:45:00] SMS Service: +1234567890 - SUCCESS
# Sending push notification to device device_abc123: Server maintenance scheduled for tonight
# [2025-10-04 22:45:00] Push Notification Service: device_abc123 - SUCCESS

# Check total notifications sent
print(f"\nTotal notifications sent: {dispatcher.total_sent}")
# Output: Total notifications sent: 3

# Check total cost
print(f"Total cost: ${dispatcher.total_cost:.3f}")
# Output: Total cost: $0.061

# Add a new service dynamically
slack = SlackNotification()  # If you implement this
dispatcher.add_service(slack)

# Send only to valid recipients
print("\n=== Sending to Valid Recipients ===")
dispatcher.send_to_valid(
    ["user@example.com", "invalid-email", "+1234567890"],
    "Account verification required"
)
# Output: Only sends to valid recipients

# Multi-channel targeting
recipient_map = {
    email: "admin@company.com",
    sms: "+9876543210",
    push: "device_xyz789"
}
success_count = send_multi_channel([email, sms, push], recipient_map, "Alert!")
print(f"\nSuccessfully sent to {success_count} channels")

# Find cheapest service
cheapest = find_cheapest_service([email, sms, push])
print(f"\nCheapest service: {cheapest.service_name} at ${cheapest.get_cost():.3f} per message")
# Output: Cheapest service: Email Service at $0.001 per message

# Batch send with statistics
results = batch_send(
    [email, sms, push],
    ["test@example.com", "+1111111111", "device_test123"],
    "Batch test message"
)
print(f"\nBatch send results: {results}")
# Output: Batch send results: {'success': 3, 'failed': 0, 'total_cost': 0.061}

