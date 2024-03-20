import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Constants
    PI = math.pi
    CONSTANT_FACTOR = 10_000_000_000

    # Calculate tire volume using the given formula
    volume = (PI * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / CONSTANT_FACTOR

    return volume

def main():
    # Get input from the user
    try:
        width = float(input("Enter the width of the tire in mm (ex 205): "))
        aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
        diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        return

    # Calculate the tire volume
    tire_volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Display the result
    print(f"\nThe approximate volume is {tire_volume:.2f} liters")

    # Get the current date
    current_date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write data to the volumes.txt file
    with open("volumes.txt", "a") as volumes_file:
        volumes_file.write(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}\n")

if __name__ == "__main__":
    main()
