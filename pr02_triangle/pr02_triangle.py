"""Triangle info."""
import math


def find_triangle_info(a, b, c):
    """
    Write a function which finds perimeter, area and type(eg: isosceles right triangle) of triangle based on given side lengths. (Note: a <= b <= c).

    The function should print "{type_by_length} {type_by_angle} triangle with perimeter of {perimeter} units and area of {area} units".
    IE: sides 3, 4, 5 should print "Scalene right triangle with perimeter of 12.0 units and area of 6.0 units".
    :return: None
    """
    if a == b == c:
        type_by_lenght = "Equilateral"
    elif a == b or a == c or b == c:
        type_by_lenght = "Isoceles"
    elif a != b != c:
        type_by_lenght = "Scalene"

    if a**2 + b**2 == c**2:
        type_by_angle = "right"
    elif a**2 + b**2 < c**2:
        type_by_angle = "obtuse"
    elif a**2 + b**2 > c**2:
        type_by_angle = "acute"

    if a == b or a == c or b == c and a**2 + b**2 > c**2:
        print(a, b, c)
    else:
        perimeter = a + b + c
        half_perimeter = (perimeter / 2)
        area = math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))
        print(f"{type_by_lenght} {type_by_angle} triangle with perimeter of {perimeter} units and area of {area} units")


if __name__ == "__main__":  # <- This line is needed for automatic testing
    find_triangle_info(4, 5, 6)
    find_triangle_info(4, 4, 6)
# Scalene acute triangle with perimeter of 15.0 units and area of 9.921567416492215 units
# Isosceles obtuse triangle with perimeter of 14.0 units and area of 7.937253933193772 units
