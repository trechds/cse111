def main():
    # Ask the user for preferred units
    units_preference = input("Do you want to calculate in Kilometers and Liters (Enter 'K') or Miles and Gallons (Enter 'M'): ").upper()

    # Get an odometer value in miles or kilometers from the user based on preference.
    if units_preference == 'M':
        start_odometer = float(input("Enter the starting odometer value in miles: "))
        end_odometer = float(input("Enter the ending odometer value in miles: "))
        fuel_amount = float(input("Enter the amount of fuel in gallons: "))
    elif units_preference == 'K':
        start_odometer = float(input("Enter the starting odometer value in kilometers: "))
        end_odometer = float(input("Enter the ending odometer value in kilometers: "))
        fuel_amount = float(input("Enter the amount of fuel in liters: "))
    else:
        print("Invalid input. Please enter 'K' for Kilometers and Liters, or 'M' for Miles and Gallons.")
        return

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_odometer, end_odometer, fuel_amount)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print("\nFuel Efficiency:")
    print(f"Miles per Gallon: {mpg:.2f} mpg")
    print(f"Liters per 100 Kilometers: {lp100k:.2f} lp/100km")

    # Convert and display results in the other unit system
    if units_preference == 'M':
        lp100k_converted = lp100k_from_mpg(mpg * 1.60934 / 3.78541)  # Convert miles to kilometers and gallons to liters
        print(f"\nConverted to Kilometers and Liters:")
        print(f"Liters per 100 Kilometers: {lp100k_converted:.2f} lp/100km")
    elif units_preference == 'K':
        mpg_converted = miles_per_gallon(start_odometer / 1.60934, end_odometer / 1.60934, fuel_amount * 3.78541)  # Convert kilometers to miles and liters to gallons
        print(f"\nConverted to Miles and Gallons:")
        print(f"Miles per Gallon: {mpg_converted:.2f} mpg")


def miles_per_gallon(start, end, gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start: An odometer value in miles or kilometers.
        end: Another odometer value in miles or kilometers.
        gallons: A fuel amount in U.S. gallons or liters.
    Return: Fuel efficiency in miles per gallon.
    """
    return (end - start) / gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()
