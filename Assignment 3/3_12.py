def print_table():
    # Print the header of the table
    print("{:<2} {:<2} {:<2} {:<3} {:<4}".format("N", "1", "N", "N^2", "N^3"))
    
    # Print the table rows
    for i in range(1, 6):
        print("{:<2} {:<2} {:<2} {:<3} {:<4}".format(i, 1, i, i**2, i**3))

# Call the function to print the table
print_table()
