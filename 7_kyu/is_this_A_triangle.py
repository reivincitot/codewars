# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).
def is_triangle(a: float, b: float, c: float) -> tuple:
    """
    Checks if three given side lengths can form a triangle.

    Args:
    - a: the length of the first side of the triangle
    - b: the length of the second side of the triangle
    - c: the length of the third side of the triangle

    Returns:
    - A tuple containing a boolean value indicating whether the given side lengths can form a triangle,
      and an optional error message if the side lengths are invalid.
    """

    # Check if any of the side lengths is less than or equal to zero
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Check if the sum of any two side lengths is greater than the third side length
    if a + b > c and a + c > b and b + c > a:
        return True

    # If neither of the above conditions is met, it is not possible to form a triangle
    return False