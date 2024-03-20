import datetime

def apply_discount(subtotal, discount_percentage):
    return subtotal * (1 - discount_percentage / 100)

def calculate_sales_tax(subtotal, tax_percentage):
    return subtotal * (tax_percentage / 100)

def main():
    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Initialize subtotal
    subtotal = 0

    # Loop to get prices and quantities until the user enters "0" for the price
    while True:
        try:
            price = float(input("Enter the price (enter 0 to finish): $"))
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")
            continue

        # Break the loop if the user enters "0" for the price
        if price == 0:
            break

        try:
            quantity = int(input("Enter the quantity: "))
        except ValueError:
            print("Invalid input. Please enter a valid numerical value for quantity.")
            continue

        subtotal += price * quantity

    # Check if it's Tuesday or Wednesday
    if current_day == "Tuesday" or current_day == "Wednesday":
        if subtotal >= 50:
            # Apply discount
            discount_percentage = 10
            discounted_subtotal = apply_discount(subtotal, discount_percentage)
            discount_amount = subtotal - discounted_subtotal

            # Calculate sales tax
            sales_tax_percentage = 6
            sales_tax_amount = calculate_sales_tax(discounted_subtotal, sales_tax_percentage)

            # Calculate total amount due
            total_amount_due = discounted_subtotal + sales_tax_amount

            # Print the results
            print("\nReceipt:")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Discount (-{discount_percentage}%): ${discount_amount:.2f}")
            print(f"Sales Tax (+{sales_tax_percentage}%): ${sales_tax_amount:.2f}")
            print(f"Total Amount Due: ${total_amount_due:.2f}")
        else:
            # Calculate and print the additional amount needed for the discount
            additional_amount_needed = 50 - subtotal
            print(f"\nAdditional amount needed for the discount: ${additional_amount_needed:.2f}")
    else:
        # Calculate sales tax for other days
        sales_tax_percentage = 6
        sales_tax_amount = calculate_sales_tax(subtotal, sales_tax_percentage)

        # Calculate total amount due for other days
        total_amount_due = subtotal + sales_tax_amount

        # Print the results
        print("\nReceipt:")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (+{sales_tax_percentage}%): ${sales_tax_amount:.2f}")
        print(f"Total Amount Due: ${total_amount_due:.2f}")

if __name__ == "__main__":
    main()
