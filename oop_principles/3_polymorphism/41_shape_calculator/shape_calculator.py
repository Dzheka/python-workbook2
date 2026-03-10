def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)


def find_largest_shape(shapes):
    return max(shapes, key=lambda s: s.area())


def filter_by_area(shapes, min_area):
    return [s for s in shapes if s.area() >= min_area]


def sort_shapes_by_area(shapes):
    return sorted(shapes, key=lambda s: s.area())


def print_shape_report(shapes):
    for shape in shapes:
        print(f"{shape.color} shape: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")
    print(f"Total area: {calculate_total_area(shapes):.2f}")
