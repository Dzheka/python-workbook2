# Pamir Mountains Trek Calculator

Calculate trek difficulty for routes in Tajikistan's Pamir Mountains using elevation, distance, and slope calculations.

## Background
The Pamir Mountains in Tajikistan include some of the world's highest peaks:
- Peak Ismoil Somoni (7,495m) - highest in Tajikistan
- Peak Lenin (7,134m)
- Peak Korzhenevskaya (7,105m)

## Input
Trek data containing:
- Starting elevation (meters)
- Ending elevation (meters)
- Horizontal distance (kilometers)

## Tasks

### Part 1: Calculate Slope Angle
Create a function `calculate_slope_angle(elevation_gain, horizontal_distance)`:
- Convert horizontal distance from km to meters
- Use `math.atan()` to find the angle in radians
- Convert radians to degrees using `math.degrees()`
- Return the slope angle in degrees

Formula: angle = atan(elevation_gain / horizontal_distance_in_meters)

### Part 2: Determine Difficulty Level
Create a function `get_difficulty(elevation, slope_angle)`:
- If elevation > 5000m OR slope_angle > 45°: return "Extreme"
- Else if elevation > 4000m OR slope_angle > 30°: return "Hard"
- Else if elevation > 3000m OR slope_angle > 15°: return "Moderate"
- Else: return "Easy"

### Part 3: Calculate Oxygen Level
Create a function `calculate_oxygen_level(elevation)`:
- Use barometric formula: oxygen% = 100 * e^(-elevation / 8000)
- Use `math.exp()` for exponential calculation
- Round to 1 decimal place

### Part 4: Assess Trek Safety
Create a function `assess_trek(start_elevation, end_elevation, distance_km)`:
- Calculate elevation_gain
- Calculate slope_angle using Part 1
- Get difficulty using Part 2
- Calculate oxygen_level at end elevation using Part 3
- Determine requires_acclimatization: True if elevation_gain > 1000m
- Return dictionary with all calculated values

## Examples

### Example 1: Trek to Peak Ismoil Somoni Base Camp
```python
result = assess_trek(4200, 5400, 8.5)
print(result)
# {
#     "elevation_gain": 1200,
#     "slope_angle": 8.04,
#     "difficulty": "Extreme",
#     "oxygen_level": 50.9,
#     "requires_acclimatization": True
# }
```

### Example 2: Easy Valley Trek
```python
result = assess_trek(2800, 3200, 12.0)
print(result)
# {
#     "elevation_gain": 400,
#     "slope_angle": 1.91,
#     "difficulty": "Moderate",
#     "oxygen_level": 67.0,
#     "requires_acclimatization": False
# }
```

### Example 3: Extreme Summit Push
```python
result = assess_trek(6000, 7495, 3.0)
print(result)
# {
#     "elevation_gain": 1495,
#     "slope_angle": 26.49,
#     "difficulty": "Extreme",
#     "oxygen_level": 39.2,
#     "requires_acclimatization": True
# }
```
