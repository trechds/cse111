# heart_rate.py

# Prompt user for age
age = int(input("Please enter your age: "))

# Calculate maximum heart rate
max_heart_rate = 220 - age

# Calculate heart rate range for strengthening the heart
min_target_rate = 0.65 * max_heart_rate
max_target_rate = 0.85 * max_heart_rate

# Display the results
print("\nTo strengthen your heart, maintain your heart rate between:")
print(f"Slowest rate: {int(min_target_rate)} beats per minute")
print(f"Fastest rate: {int(max_target_rate)} beats per minute")
