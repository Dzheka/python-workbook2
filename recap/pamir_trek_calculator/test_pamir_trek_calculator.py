import math
from pamir_trek_calculator import (
    calculate_slope_angle,
    get_difficulty,
    calculate_oxygen_level,
    assess_trek
)


def test_calculate_slope_angle_flat():
    angle = calculate_slope_angle(100, 10.0)
    assert angle == 0.57


def test_calculate_slope_angle_steep():
    angle = calculate_slope_angle(1000, 1.0)
    assert angle == 45.0


def test_calculate_slope_angle_moderate():
    angle = calculate_slope_angle(1200, 8.5)
    assert angle == 8.04


def test_get_difficulty_easy():
    assert get_difficulty(2500, 10) == "Easy"
    assert get_difficulty(2999, 14) == "Easy"
    assert get_difficulty(3000, 10) == "Easy"


def test_get_difficulty_moderate():
    assert get_difficulty(3001, 10) == "Moderate"
    assert get_difficulty(3500, 20) == "Moderate"
    assert get_difficulty(2500, 16) == "Moderate"
    assert get_difficulty(3500, 30) == "Moderate"


def test_get_difficulty_hard():
    assert get_difficulty(4001, 10) == "Hard"
    assert get_difficulty(4500, 25) == "Hard"
    assert get_difficulty(3500, 31) == "Hard"
    assert get_difficulty(5000, 10) == "Hard"


def test_get_difficulty_extreme():
    assert get_difficulty(5001, 10) == "Extreme"
    assert get_difficulty(7000, 20) == "Extreme"
    assert get_difficulty(4000, 46) == "Extreme"
    assert get_difficulty(3000, 50) == "Extreme"


def test_calculate_oxygen_level_sea_level():
    oxygen = calculate_oxygen_level(0)
    assert oxygen == 100.0


def test_calculate_oxygen_level_high_altitude():
    oxygen = calculate_oxygen_level(5400)
    assert oxygen == 50.9


def test_calculate_oxygen_level_extreme():
    oxygen = calculate_oxygen_level(7495)
    assert oxygen == 39.2


def test_assess_trek_base_camp():
    result = assess_trek(4200, 5400, 8.5)

    assert result["elevation_gain"] == 1200
    assert result["slope_angle"] == 8.04
    assert result["difficulty"] == "Extreme"
    assert result["oxygen_level"] == 50.9
    assert result["requires_acclimatization"] == True


def test_assess_trek_valley():
    result = assess_trek(2800, 3200, 12.0)

    assert result["elevation_gain"] == 400
    assert result["slope_angle"] == 1.91
    assert result["difficulty"] == "Moderate"
    assert result["oxygen_level"] == 67.0
    assert result["requires_acclimatization"] == False


def test_assess_trek_summit():
    result = assess_trek(6000, 7495, 3.0)

    assert result["elevation_gain"] == 1495
    assert result["slope_angle"] == 26.49
    assert result["difficulty"] == "Extreme"
    assert result["oxygen_level"] == 39.2
    assert result["requires_acclimatization"] == True


def test_assess_trek_easy():
    result = assess_trek(1500, 1800, 5.0)

    assert result["elevation_gain"] == 300
    assert result["slope_angle"] == 3.43
    assert result["difficulty"] == "Easy"
    assert result["oxygen_level"] == 79.9
    assert result["requires_acclimatization"] == False


def test_assess_trek_acclimatization_boundary():
    # Exactly 1000m should not require acclimatization
    result = assess_trek(3000, 4000, 10.0)
    assert result["requires_acclimatization"] == False

    # 1001m should require acclimatization
    result = assess_trek(3000, 4001, 10.0)
    assert result["requires_acclimatization"] == True


def test_assess_trek_difficulty_boundaries():
    # Test boundary at 3000m - exactly 3000 is not > 3000, so it's Easy
    result1 = assess_trek(2000, 3000, 10.0)
    assert result1["difficulty"] == "Easy"

    result2 = assess_trek(2000, 3001, 10.0)
    assert result2["difficulty"] == "Moderate"

    # Test boundary at 4000m - exactly 4000 is not > 4000
    result3 = assess_trek(3000, 4000, 10.0)
    assert result3["difficulty"] == "Moderate"

    result4 = assess_trek(3000, 4001, 10.0)
    assert result4["difficulty"] == "Hard"

    # Test boundary at 5000m - exactly 5000 is not > 5000
    result5 = assess_trek(4000, 5000, 10.0)
    assert result5["difficulty"] == "Hard"

    result6 = assess_trek(4000, 5001, 10.0)
    assert result6["difficulty"] == "Extreme"
