class Clock:
    def __init__(self, hour, minute):
        total = hour * 60 + minute
        total = total % (24 * 60)
        self._hour = total // 60
        self._minute = total % 60

    def add_minutes(self, minutes):
        total = self._hour * 60 + self._minute + minutes
        total = total % (24 * 60)
        self._hour = total // 60
        self._minute = total % 60

    def subtract_minutes(self, minutes):
        self.add_minutes(-minutes)

    def __str__(self):
        return f"{self._hour:02d}:{self._minute:02d}"

    def __repr__(self):
        return f"Clock({self._hour}, {self._minute})"

    def __eq__(self, other):
        return self._hour == other._hour and self._minute == other._minute
