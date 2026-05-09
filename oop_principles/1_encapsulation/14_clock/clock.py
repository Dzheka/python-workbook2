class Clock:
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        if total_minutes < 0:
            while total_minutes < 0:
                total_minutes += 24 * 60
        elif total_minutes >= 24 * 60:
            while total_minutes >= 24 * 60:
                total_minutes -= 24*60
        self._hour = total_minutes // 60
        self._minute = total_minutes % 60

    def add_minutes(self, minutes):
        total_minutes = self._hour*60 + self._minute + minutes
        if total_minutes < 0:
            while total_minutes < 0:
                total_minutes += 24 * 60
        elif total_minutes >= 24 * 60:
            while total_minutes >= 24 * 60:
                total_minutes -= 24*60
        self._hour = total_minutes // 60
        self._minute = total_minutes % 60

    def subtract_minutes(self, minutes):
        self.add_minutes(-minutes)

    def __str__(self):
        return f"{self._hour}:{self._minute}"
    
    def __repr__(self):
        return f"Clock({self._hour}, {self._minute})"
    
    def __eq__(self, other):
        return self._hour == other._hour and self._minute == other._minute
    
clock1 = Clock(11, 30)
clock2 = Clock(11, 30)
print(str(clock1))      # 11:30
print(repr(clock1))     # Clock(11, 30)
print(clock1 == clock2) # True

clock3 = Clock(12, 0)
print(clock1 == clock3) # False

clock1.add_minutes(60)
print(clock1)           # 12:30
clock1.subtract_minutes(120)
print(clock1)           # 10:30