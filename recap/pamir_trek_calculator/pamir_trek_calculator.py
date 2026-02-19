import math


def calculate_slope_angle(elevation_gain, horizontal_distance_km):
    """ your code """


def get_difficulty(elevation, slope_angle):
        """ your code """



def calculate_oxygen_level(elevation):
    """ your code """


def assess_trek(start_elevation, end_elevation, distance_km):
    """ your code """


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
