# boxes.py

import math

# Prompt user for inputs
num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed using math.ceil() to ensure a whole number
num_boxes = math.ceil(num_items / items_per_box)

# Display the result
print(f"\nFor {num_items} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes.")
