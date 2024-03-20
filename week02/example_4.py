# Example 4

import math

# Get the radius and height from the user.
radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of a cylinder: "))

# Compute the volume of the cylinder.
volume = math.pi * radius**2 * height

# Print the volume of the cylinder.
print(f"Volume: {volume:.2f}")