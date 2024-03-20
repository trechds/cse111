# Example 6

# Get an account balance as a number from the user.
balance = float(input("Enter the account balance: "))

# If the balance is greater than 500, then
# compute and add interest to the balance.
if balance > 500:
    interest = balance * 0.03
    balance += interest

# Print the balance.
print(f"balance: {balance:.2f}")