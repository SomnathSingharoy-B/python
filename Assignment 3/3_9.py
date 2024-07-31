def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "/ \\" * i)
        print(" " * (n - i) + "/_" * i + "\\")

# Example usage:
try:
    N = int(input("Enter the number of lines N: "))
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    print_pattern(N)
except ValueError as e:
    print(e)
