import math


def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def print_circle_area(radius):
    """
    Print the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.
    """
    try:
        area = calculate_circle_area(radius)
        print(f"The area of a circle with radius {radius} is {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    """
    Main function to execute the program.
    """
    radius_list = [3, 4.5, -2, 10]

    for radius in radius_list:
        print_circle_area(radius)


if __name__ == "__main__":
    main()

