class Clock:
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        total_minutes %= 24 * 60
        self._hour = total_minutes
        self._minute = total_minutes