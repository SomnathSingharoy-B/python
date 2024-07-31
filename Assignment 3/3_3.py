import cmath

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero in a quadratic equation.")

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two solutions
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    # If the roots are real, return them as real numbers
    if discriminant >= 0:
        return (root1.real, root2.real)
    else:
        return (root1, root2)

# Example usage:
try:
    print(solve_quadratic_eqn(1, -3, 2))   # Output: (2.0, 1.0) - Two distinct real roots
    print(solve_quadratic_eqn(1, 2, 1))    # Output: (-1.0, -1.0) - One real root
    print(solve_quadratic_eqn(1, 0, 1))    # Output: (1j, -1j) - Two complex roots
except ValueError as e:
    print(e)
