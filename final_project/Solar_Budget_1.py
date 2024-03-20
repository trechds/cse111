import tkinter as tk

def main():
    print("Welcome to the Solar Energy Budget Calculation Program")

    # Create the main window
    window = tk.Tk()
    window.title("Solar Energy Budget Calculator")

    # Ask user for customer information
    customer_name = input("Enter customer's full name: ")
    phone_number = input("Enter customer's phone number: ")
    email = input("Enter customer's email: ")
    city_state = input("Enter customer's city-state: ")
    seller_name = input("Enter seller's name: ")
    mains_phase = input("Select mains phase (Single-phase/Biphasic/Three-phase): ")
    energy_utility = input("Enter Energy Utility (CPFL/RGE/Coprel/Cerfox): ")

    # Ask user for energy consumption in kWh for each month
    energy_consumption = {}
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for month in months:
        consumption = input(f"Enter energy consumption in kWh for {month} (press Enter if no consumption): ")
        if consumption:
            energy_consumption[month] = float(consumption)

    # Ask user to select panel installation structure
    panel_structure = input("Select panel installation structure (Brasilite/Aluzinc/Ceramic/Ground/Slab): ")
    # Ask the user to select the panel installation structure
    determine_roof_type()

    # Close the main windowbr
    window.destroy()

    # Call function to calculate budget with user inputs
    calculate_budget(customer_name, phone_number, email, city_state, seller_name, mains_phase, energy_utility, energy_consumption, panel_structure)

def calculate_average_energy_consumption(energy_consumption):
    # Verifica se há dados de consumo de energia
    if not energy_consumption:
        return 0
    
    # Calcula a média dos valores de consumo de energia
    total_consumption = sum(energy_consumption.values())
    average_consumption = total_consumption / len(energy_consumption)
    
    return average_consumption

# Chama a função para calcular a média de consumo de energia
average_consumption = calculate_average_energy_consumption(energy_consumption)
print("Average energy consumption across the months:", average_consumption, "kWh")


def determine_roof_type():
    # Create a dictionary mapping roof types to structure types and prices
    roof_types = {
        "Brasilite": {"structure_type": "Mini Rail 24cm", "price_per_module": 30},
        "Aluzinc": {"structure_type": "Mini Rail 40cm", "price_per_module": 45},
        "Ceramic": {"structure_type": "Colonial", "price_per_module": 130},
        "Ground": {"structure_type": "Block", "price_per_module": 120},
        "Slab": {"structure_type": "Steel", "price_per_module": 150}
    }

    # Print the available roof types
    print("Available Roof Types:")
    for roof_type in roof_types:
        print(roof_type)

    # Ask the user to select a roof type
    selected_roof = input("Select a roof type: ")

    # Check if the selected roof type is valid
    if selected_roof in roof_types:
        # Retrieve structure type and price for the selected roof type
        structure_type = roof_types[selected_roof]["structure_type"]
        price_per_module = roof_types[selected_roof]["price_per_module"]
        print(f"Structure Type: {structure_type}")
        print(f"Price per Solar Module: R${price_per_module}")
    else:
        print("Invalid roof type selected.")

# Test the function
determine_roof_type()

def determine_panel_orientation():
    guidance_radiation = {
    "North": 112,
    "Northeast": 110,
    "Northwest": 110,
    "East": 104,
    "West": 104,
    "South": 95,
    "Southeast": 100,
    "Southwest": 100
}
    pass

def calculate_energy_consumption():
    # Placeholder function for calculating energy consumption
    pass

def calculate_panel_quantity():
    # Placeholder function for calculating panel quantity
    pass

def calculate_inverter():
    # Placeholder function for calculating inverters
    pass

def define_panel_area():
    # Placeholder function for defining panel area
    pass

def determine_inverter_type():
    # Placeholder function for determining inverter type
    pass

def define_panel_structure():
    # Placeholder function for defining panel structure
    pass

def calculate_budget():
    # Placeholder function for calculating budget
    pass

def calculate_energy_generation():
    # Calculate Power to be installed (kWp) for each orientation
    power_installed = {}
    for orientation, irradiation in guidance_radiation.items():
        power_installed[orientation] = average_consumption / irradiation

    # Define the module power (Watts)
    module_power = 320  # Example value, change as needed

    # Calculate Average Monthly Generation for each orientation
    monthly_generation = {}
    for orientation, power in power_installed.items():
        monthly_generation[orientation] = power * module_power / 1000

    # Print the results
    print("Power to be installed (kWp) for each orientation:")
    for orientation, power in power_installed.items():
        print(f"{orientation}: {power:.2f} kWp")

    print("\nAverage Monthly Generation for each orientation:")
    for orientation, generation in monthly_generation.items():
        print(f"{orientation}: {generation:.2f} kWh")
    pass

def generate_proposal():
    # Placeholder function for generating proposal
    pass

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Solar Energy Budget Calculator")

    # Labels and entry fields for user input
    roof_label = tk.Label(window, text="Roof Type:")
    roof_label.grid(row=0, column=0, padx=10, pady=5)
    roof_entry = tk.Entry(window)
    roof_entry.grid(row=0, column=1, padx=10, pady=5)

    orientation_label = tk.Label(window, text="Panel Orientation:")
    orientation_label.grid(row=1, column=0, padx=10, pady=5)
    orientation_entry = tk.Entry(window)
    orientation_entry.grid(row=1, column=1, padx=10, pady=5)

    kWh_label = tk.Label(window, text="Energy Consumption (kWh):")
    kWh_label.grid(row=2, column=0, padx=10, pady=5)
    kWh_entry = tk.Entry(window)
    kWh_entry.grid(row=2, column=1, padx=10, pady=5)

    # Button to calculate budget
    calculate_button = tk.Button(window, text="Calculate Budget", command=calculate_budget)
    calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)

    # Run the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
