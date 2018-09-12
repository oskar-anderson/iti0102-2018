"""Circle info."""
import math


def find_circle_info(d, x, y):
    """
    Find perimeter, area and where given point is placed in relation to the circle with diameter d.

    Place: inside, perimeter, outside.
    The function should print "Circle with perimeter of {perimeter} units and area of {area} units has point
    ({x}, {y}) on its {place}".
    :return: None
    """
    perimeter = d * math.pi
    area = pow((d / 2), 2) * math.pi
    if d / 2 > math.sqrt(x**2 + y**2):
        place = "inside"
    elif d / 2 == math.sqrt(x**2 + y**2):
        place = "perimeter"
    else:
        place = "outside"
    print(f"Circle with perimeter of {perimeter} units and area of {area} units has point ({x}, {y}) on its {place}.")


if __name__ == "__main__":  # <- This line is needed for automatic testing
    find_circle_info(10, 9, 8)
    # Circle with perimeter of 31.41592653589793 units and area of 78.53981633974483 units has point
    # (9, 8) on its outside
