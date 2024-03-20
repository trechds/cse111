import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Constants
    PI = math.pi
    CONSTANT_FACTOR = 10_000_000_000

    # Calculate tire volume using the given formula
    volume = (PI * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / CONSTANT_FACTOR

    return volume

def get_tire_price(width, aspect_ratio, diameter):
    # Add logic to determine tire prices based on tire dimensions
    if width == 185 and aspect_ratio == 50 and diameter == 14:
        return 100
    elif width == 205 and aspect_ratio == 60 and diameter == 15:
        return 120
    elif width == 215 and aspect_ratio == 65 and diameter == 16:
        return 150
    elif width == 230 and aspect_ratio == 70 and diameter == 17:
        return 180
    else:
        return 200

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

    # Get tire price based on dimensions
    tire_price = get_tire_price(width, aspect_ratio, diameter)
    print(f"Tire price: ${tire_price}")

    # Ask the user if they want to buy the tires
    buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

    if buy_tires == "yes":
        # Ask for the user's phone number
        phone_number = input("Enter your phone number: ")

        # Get the current date and time
        current_date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write data to the volumes.txt file, including phone number
        with open("volumes.txt", "a") as volumes_file:
            volumes_file.write(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}, {phone_number}\n")

        print("Thank you! Your order has been placed.")
    else:
        print("Thank you for using the tire volume calculator.")
        
if __name__ == "__main__":
    main()