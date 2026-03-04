import math


def calculate_slope_angle(elevation_gain, horizontal_distance):
    horizontal_distance_m = horizontal_distance * 1000
    angle_rad = math.atan(elevation_gain / horizontal_distance_m)
    return round(math.degrees(angle_rad), 2)


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


if __name__ == "__main__":
    print(assess_trek(4200, 5400, 8.5))
    print(assess_trek(2800, 3200, 12.0))
    print(assess_trek(6000, 7495, 3.0))
