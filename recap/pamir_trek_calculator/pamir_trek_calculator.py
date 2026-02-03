import math


def calculate_slope_angle(elevation_gain, horizontal_distance_km):
    horizontal_distance_in_meters = horizontal_distance_km * 1000
    angle_radians = math.atan(elevation_gain / horizontal_distance_in_meters)
    angle_degrees = math.degrees(angle_radians)
    return round(angle_degrees, 2)


def get_difficulty(elevation, slope_angle):
    if elevation > 5000 or slope_angle > 45:
        return "Extreme"
    elif elevation > 4000 or slope_angle > 30:
        return "Hard"
    elif elevation > 3000 or slope_angle > 15:
        return "Moderate"
    else:
        return "Easy"



def calculate_oxygen_level(elevation):
    oxygen_percent = 100*math.exp(-elevation/8000)
    return round(oxygen_percent, 1)


def assess_trek(start_elevation, end_elevation, distance_km):
    elevation_gain = end_elevation - start_elevation
    slope_angle = calculate_slope_angle(elevation_gain, distance_km)
    difficulty = get_difficulty(end_elevation, slope_angle)
    oxygen_level = calculate_oxygen_level(end_elevation)
    requires_acclimatization = elevation_gain > 1000
    return {
        "elevation_gain": elevation_gain,
        "slope_angle": slope_angle,
        "difficulty": difficulty,
        "oxygen_level": oxygen_level,
        "requires_acclimatization": requires_acclimatization
        }


def main():
    print("=== Pamir Mountains Trek Calculator ===\n")

    # Trek 1: Peak Ismoil Somoni Base Camp
    print("Trek to Peak Ismoil Somoni Base Camp:")
    result1 = assess_trek(4200, 5400, 8.5)
    print(f"  Elevation gain: {result1['elevation_gain']}m")
    print(f"  Slope angle: {result1['slope_angle']}°")
    print(f"  Difficulty: {result1['difficulty']}")
    print(f"  Oxygen level: {result1['oxygen_level']}%")
    print(f"  Acclimatization needed: {result1['requires_acclimatization']}\n")

    # Trek 2: Easy Valley Trek
    print("Easy Valley Trek:")
    result2 = assess_trek(2800, 3200, 12.0)
    print(f"  Elevation gain: {result2['elevation_gain']}m")
    print(f"  Slope angle: {result2['slope_angle']}°")
    print(f"  Difficulty: {result2['difficulty']}")
    print(f"  Oxygen level: {result2['oxygen_level']}%")
    print(f"  Acclimatization needed: {result2['requires_acclimatization']}\n")

    # Trek 3: Extreme Summit Push
    print("Extreme Summit Push to Peak Ismoil Somoni:")
    result3 = assess_trek(6000, 7495, 3.0)
    print(f"  Elevation gain: {result3['elevation_gain']}m")
    print(f"  Slope angle: {result3['slope_angle']}°")
    print(f"  Difficulty: {result3['difficulty']}")
    print(f"  Oxygen level: {result3['oxygen_level']}%")
    print(f"  Acclimatization needed: {result3['requires_acclimatization']}")


if __name__ == "__main__":
    main()
