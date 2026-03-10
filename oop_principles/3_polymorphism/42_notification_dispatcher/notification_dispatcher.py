class NotificationDispatcher:
    def __init__(self, services):
        self.services = list(services)
        self._total_cost = 0

    def add_service(self, service):
        self.services.append(service)

    def remove_service(self, service):
        self.services.remove(service)

    def broadcast(self, recipients, message):
        for service in self.services:
            for recipient in recipients:
                result = service.send(recipient, message)
                if result:
                    self._total_cost += service.get_cost()

    def send_to_valid(self, recipients, message):
        for service in self.services:
            for recipient in recipients:
                if service.validate_recipient(recipient):
                    result = service.send(recipient, message)
                    if result:
                        self._total_cost += service.get_cost()

    @property
    def total_sent(self):
        return sum(s.sent_count for s in self.services)

    @property
    def total_cost(self):
        return self._total_cost


def send_multi_channel(services, recipient_map, message):
    count = 0
    for service in services:
        if service in recipient_map:
            result = service.send(recipient_map[service], message)
            if result:
                count += 1
    return count


def find_cheapest_service(services):
    return min(services, key=lambda s: s.get_cost())


def batch_send(services, recipients, message):
    success = 0
    failed = 0
    total_cost = 0
    for service in services:
        for recipient in recipients:
            result = service.send(recipient, message)
            if result:
                success += 1
                total_cost += service.get_cost()
            else:
                failed += 1
    return {"success": success, "failed": failed, "total_cost": total_cost}
