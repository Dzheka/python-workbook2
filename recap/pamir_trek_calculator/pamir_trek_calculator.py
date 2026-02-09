import math

def calculate_slope_angle(gain, dist_km):
    dist_m = dist_km * 1000
    ang = math.atan(gain / dist_m)
    return round(math.degrees(ang), 2)

def get_difficulty(elev, ang):
    if elev > 5000 or ang > 45:
        return "Extreme"
    elif elev > 4000 or ang > 30:
        return "Hard"
    elif elev > 3000 or ang > 15:
        return "Moderate"
    else:
        return "Easy"

def calculate_oxygen_level(elev):
    oxy = 100 * math.exp(-elev / 8000)
    return round(oxy, 1)

def assess_trek(start, end, dist_km):
    gain = end - start
    ang = calculate_slope_angle(gain, dist_km)
    diff = get_difficulty(end, ang)
    oxy = calculate_oxygen_level(end)
    accl = gain > 1000
    return {
        "elevation_gain": gain,
        "slope_angle": ang,
        "difficulty": diff,
        "oxygen_level": oxy,
        "requires_acclimatization": accl,
    }

def main():
    print("=== Pamir Mountains Trek Calculator ===\n")

    print("Trek to Peak Ismoil Somoni Base Camp:")
    r1 = assess_trek(4200, 5400, 8.5)
    print(r1, "\n")

    print("Easy Valley Trek:")
    r2 = assess_trek(2800, 3200, 12.0)
    print(r2, "\n")

    print("Extreme Summit Push to Peak Ismoil Somoni:")
    r3 = assess_trek(6000, 7495, 3.0)
    print(r3)

if __name__ == "__main__":
    main()