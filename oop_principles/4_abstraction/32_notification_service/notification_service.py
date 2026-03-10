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

    def get_cost(self):
        return 0.001

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending email to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class SMSNotification(NotificationService):
    def __init__(self):
        super().__init__("SMS Service")

    def validate_recipient(self, recipient):
        return recipient.startswith("+")

    def get_cost(self):
        return 0.05

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending SMS to {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True


class PushNotification(NotificationService):
    def __init__(self):
        super().__init__("Push Notification Service")

    def validate_recipient(self, recipient):
        return len(recipient) > 5

    def get_cost(self):
        return 0.01

    def send(self, recipient, message):
        if not self.validate_recipient(recipient):
            self.log_notification(recipient, "FAILED")
            return False
        print(f"Sending push notification to device {recipient}: {message}")
        self.log_notification(recipient, "SUCCESS")
        return True
