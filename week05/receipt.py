import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError:
        print("Error: missing file")
        raise
    return dictionary

def main():
    try:
        # Read products dictionary from products.csv
        products_dict = read_dictionary("products.csv", 0)

        # Print store name
        print("Inkom Emporium\n")

        # Open request.csv and process each row
        print("Ordered Items")
        subtotal = 0
        total_items = 0
        with open("request.csv", newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                product_number, quantity = row
                product_info = products_dict.get(product_number.upper())  # Ensure product number is uppercase
                if product_info:
                    product_name, _, price = product_info
                    total_price = float(price) * int(quantity)
                    print(f"{product_name.lower()}: {quantity} @ {price}")
                    subtotal += total_price
                    total_items += int(quantity)
                else:
                    print(f"Error: unknown product ID in the request.csv file\n'{product_number}'")
    except PermissionError:
        print("Error: permission denied")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n'{e.args[0]}'")

    # Apply discount if today is Tuesday or Wednesday
    today = datetime.now().weekday()
    if today == 1 or today == 2:  # Tuesday is 1, Wednesday is 2
        print("\nApplying 10% discount for orders placed on Tuesday or Wednesday.")
        discount = subtotal * 0.10
        subtotal -= discount

    # Compute sales tax and total
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax

    # Print summary
    print(f"\nNumber of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}\n")

    # Print thank you message and current date and time
    print("Thank you for shopping at the Inkom Emporium.")
    current_date_and_time = datetime.now()
    print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))


if __name__ == "__main__":
    main()