import math


def calculate_slope_angle(elevation_gain, distance_km):
    distance_m = distance_km * 1000
    angle = math.degrees(math.atan(elevation_gain / distance_m))
    return round(angle, 2)

def get_difficulty(elevation, slope_angle):
    if elevation > 5000 or slope_angle > 45:
        return "Extreme"
    if elevation > 4000 or slope_angle > 30:
        return "Hard"
    if elevation > 3000 or slope_angle > 15:
        return "Moderate"
    return "Easy"

def calculate_oxygen_level(elevation):
    oxygen = 100 * math.exp(-elevation / 8000)
    return round(oxygen, 1)

def assess_trek(start_elevation, end_elevation, distance_km):
    gain = end_elevation - start_elevation
    angle = calculate_slope_angle(gain, distance_km)
    difficulty = get_difficulty(end_elevation, angle)
    oxygen = calculate_oxygen_level(end_elevation)
    acclimatization = gain > 1000

    return {
        "elevation_gain": gain,
        "slope_angle": angle,
        "difficulty": difficulty,
        "oxygen_level": oxygen,
        "requires_acclimatization": acclimatization
    }

def main():
    print(assess_trek(4200, 5400, 8.5))
    print(assess_trek(2800, 3200, 12.0))
    print(assess_trek(6000, 7495, 3.0))



def main():
    print("=== Pamir Mountains Trek Calculator ===\n")

    print("Trek to Peak Ismoil Somoni Base Camp:")
    result1 = assess_trek(4200, 5400, 8.5)
    print(f"  Elevation gain: {result1['elevation_gain']}m")
    print(f"  Slope angle: {result1['slope_angle']}°")
    print(f"  Difficulty: {result1['difficulty']}")
    print(f"  Oxygen level: {result1['oxygen_level']}%")
    print(f"  Acclimatization needed: {result1['requires_acclimatization']}\n")

    print("Easy Valley Trek:")
    result2 = assess_trek(2800, 3200, 12.0)
    print(f"  Elevation gain: {result2['elevation_gain']}m")
    print(f"  Slope angle: {result2['slope_angle']}°")
    print(f"  Difficulty: {result2['difficulty']}")
    print(f"  Oxygen level: {result2['oxygen_level']}%")
    print(f"  Acclimatization needed: {result2['requires_acclimatization']}\n")

    print("Extreme Summit Push to Peak Ismoil Somoni:")
    result3 = assess_trek(6000, 7495, 3.0)
    print(f"  Elevation gain: {result3['elevation_gain']}m")
    print(f"  Slope angle: {result3['slope_angle']}°")
    print(f"  Difficulty: {result3['difficulty']}")
    print(f"  Oxygen level: {result3['oxygen_level']}%")
    print(f"  Acclimatization needed: {result3['requires_acclimatization']}")


if __name__ == "__main__":
    main()
