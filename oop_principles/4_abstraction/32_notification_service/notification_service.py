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
    
# This should fail - cannot instantiate abstract class
try:
    service = NotificationService("Generic")
except TypeError as e:
    print(f"Error: {e}")

# Create concrete services
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

# Send notifications
email.send("user@example.com", "Hello!")
# Output: Sending email to user@example.com: Hello!
#         [2025-10-02 07:50:00] Email Service: user@example.com - SUCCESS

sms.send("+1234567890", "Verification code: 123456")
# Output: Sending SMS to +1234567890: Verification code: 123456
#         [2025-10-02 07:50:00] SMS Service: +1234567890 - SUCCESS

push.send("device_abc123", "New message received")
# Output: Sending push notification to device device_abc123: New message received
#         [2025-10-02 07:50:00] Push Notification Service: device_abc123 - SUCCESS

# Invalid recipients
email.send("invalid-email", "Test")
# Output: [2025-10-02 07:50:00] Email Service: invalid-email - FAILED

sms.send("1234567890", "Test")  # Missing +
# Output: [2025-10-02 07:50:00] SMS Service: 1234567890 - FAILED

push.send("dev1", "Test")  # Too short
# Output: [2025-10-02 07:50:00] Push Notification Service: dev1 - FAILED

# Check costs
print(f"Email cost: ${email.get_cost():.3f}")  # $0.001
print(f"SMS cost: ${sms.get_cost():.3f}")      # $0.050
print(f"Push cost: ${push.get_cost():.3f}")    # $0.010

# Track sent count
print(f"Emails sent: {email.sent_count}")  # 1
print(f"SMS sent: {sms.sent_count}")       # 1
print(f"Push sent: {push.sent_count}")     # 1

# Function that works with ANY notification service
def send_batch(service: NotificationService, recipients, message):
    for recipient in recipients:
        service.send(recipient, message)
    total_cost = service.sent_count * service.get_cost()
    print(f"Total sent: {service.sent_count}, Total cost: ${total_cost:.2f}")

# Works with any service
send_batch(email, ["alice@test.com", "bob@test.com"], "Batch message")
send_batch(sms, ["+1111111111", "+2222222222"], "Batch SMS")
send_batch(push, ["device_xyz789", "device_abc456"], "Batch push")