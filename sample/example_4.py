# Example 4

# Compute the total price of a pizza.

# The base price of a large pizza is $10.95
price = 10.95

# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))

# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping

# Add the cost of the toppings to the price of the pizza.
price = price + toppings_cost

# Print the price for the user to see.
print(f"Price: ${price:.2f}")