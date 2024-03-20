# Example 3

# Given the distance that a cable will span and the distance
# it will sag or dip in the middle, this program computes the
# length of the cable.

# Get user input and convert it from
# strings to floating point numbers.
span = float(input("Distance the cable must span in meters: "))
dip = float(input("Distance the cable will sag in meters: "))

# Use the numbers to compute the cable length.
length = span + (8 * dip**2) / (3 * span)

# Print the cable length in the
# console window for the user to see.
print(f"Length of cable in meters: {length:.2f}")