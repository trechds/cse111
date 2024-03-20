import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import datetime
import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Determined Variables Costs
cost_km = 1.20
food_per_person = 25
hotel_per_person = 80
cost_hour_man = 25

def main():
    """
    Main function to create the GUI for generating a solar energy proposal.
    """
    root = tk.Tk()
    root.title("Solar Energy Proposal Generator")

    # Customer information
    tk.Label(root, text="Customer Name:").grid(row=0, column=0, sticky="w")
    customer_name_entry = tk.Entry(root)
    customer_name_entry.grid(row=0, column=1)

    tk.Label(root, text="Customer City:").grid(row=1, column=0, sticky="w")
    customer_city_entry = tk.Entry(root)
    customer_city_entry.grid(row=1, column=1)

    tk.Label(root, text="Average Energy Consumption (kWh):").grid(row=2, column=0, sticky="w")
    energy_consumption_entry = tk.Entry(root)
    energy_consumption_entry.grid(row=2, column=1)

    # Phase selection
    tk.Label(root, text="Phase:").grid(row=3, column=0, sticky="w")
    phase_combo = ttk.Combobox(root, values=["Single-phase", "Biphasic", "Three-phase"])
    phase_combo.grid(row=3, column=1)

    # Roof type selection
    tk.Label(root, text="Roof Type:").grid(row=4, column=0, sticky="w")
    roof_type_combo = ttk.Combobox(root, values=["Brasilite", "Aluzinc", "Ceramic", "Ground", "Slab"])
    roof_type_combo.grid(row=4, column=1)

    # Orientation selection
    tk.Label(root, text="Orientation:").grid(row=5, column=0, sticky="w")
    orientation_combo = ttk.Combobox(root, values=["North", "Northeast", "Northwest", "East", "West", "South", "Southeast", "Southwest"])
    orientation_combo.grid(row=5, column=1)

    # Module power selection
    tk.Label(root, text="Module Power (Watts):").grid(row=6, column=0, sticky="w")
    module_power_entry = ttk.Combobox(root, values=["550", "500", "450", "400", "350", "300",])
    module_power_entry.grid(row=6, column=1)

    # Button to generate proposal
    generate_button = tk.Button(root, text="Generate Proposal", command=lambda: generate_proposal(customer_name_entry.get(), customer_city_entry.get(), int(energy_consumption_entry.get()), phase_combo.get(), roof_type_combo.get(), orientation_combo.get(), int(module_power_entry.get())))
    generate_button.grid(row=7, columnspan=2)

    root.mainloop()

def determine_irradiation(orientation):
    """
    Function to determine the irradiation based on the panel orientation.

    Args:
        orientation (str): The selected panel orientation.

    Returns:
        int: The irradiation value for the given orientation.
    """
    orientation_irradiation = {
        "North": 112,
        "Northeast": 110,
        "Northwest": 110,
        "East": 104,
        "West": 104,
        "South": 95,
        "Southeast": 100,
        "Southwest": 100
    }
    return orientation_irradiation.get(orientation, 0)

def calculate_required_power(energy_consumption_average, irradiation):
    """
    Function to calculate the required power.

    Args:
        energy_consumption_average (int): Average energy consumption per month in kWh.
        irradiation (int): Irradiation value based on panel orientation.

    Returns:
        float: Required power in kW.
    """
    return energy_consumption_average / irradiation

def determine_module_quantity(energy_consumption_average, irradiation, module_power):
    """
    Function to determine the quantity of modules required.

    Args:
        energy_consumption_average (int): Average energy consumption per month in kWh.
        irradiation (int): Irradiation value based on panel orientation.
        module_power (int): Power of each module in watts.

    Returns:
        int: The quantity of modules required.
    """
    module_quantity = math.ceil((energy_consumption_average * 1.3) / irradiation * 1000 / module_power)
    return module_quantity

def calculate_total_power(module_quantity, module_power):
    """
    Function to calculate the total power.

    Args:
        module_quantity (int): The quantity of modules required.
        module_power (int): Power of each module in watts.

    Returns:
        float: Total power in kW.
    """
    return module_quantity * module_power / 1000

def get_average_monthly_generation(total_power, irradiation, energy_consumption_average):
    """
    Function to get the average monthly generation and percentage surplus.

    Args:
        total_power (float): Total power in kW.
        irradiation (int): Irradiation value based on panel orientation.
        energy_consumption_average (int): Average energy consumption per month in kWh.

    Returns:
        tuple: A tuple containing the average monthly generation and percentage surplus.
    """
    generation = total_power * irradiation
    difference = generation - energy_consumption_average
    percentage = (difference / energy_consumption_average) * 100
    return generation, percentage

def calculate_inverter_power(total_power):
    """
    Function to calculate the inverter power.

    Args:
        total_power (float): Total power in kW.

    Returns:
        float: Inverter power in kW.
    """
    overload = 0.30
    inverter_power = total_power / (1 + overload)
    power_inverters = [0.6, 1, 1.3, 1.6, 2, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 33, 35, 40, 45, 50, 60, 75, 100]
    return min(power_inverters, key=lambda x:abs(x-inverter_power))

def determine_inverter_phase(inverter_power):
    """
    Function to determine the inverter phase.

    Args:
        inverter_power (float): Inverter power in kW.

    Returns:
        str: The phase of the inverter.
    """
    if inverter_power <= 5:
        return "Single-phase"
    elif inverter_power <= 15:
        return "Biphasic"
    else:
        return "Three-phase"

def determine_inverter_quantity(phase, inverter_power):
    """
    Function to determine the quantity of inverters required.

    Args:
        phase (str): The main phase at the establishment (single-phase, biphasic, or three-phase).
        inverter_power (float): Inverter power in kW.

    Returns:
        int: The quantity of inverters required.
    """
    if phase == "Three-phase":
        return math.ceil(inverter_power / 10)
    else:
        return math.ceil(inverter_power / 6)

def calculate_distance(customer_city):
    """
    Function to calculate the distance between the customer city and the company location.

    Args:
        customer_city (str): The city where the installation will take place.

    Returns:
        float: The distance in kilometers.
    """
    geolocator = Nominatim(user_agent="proposal_generator")
    customer_location = geolocator.geocode(customer_city)
    company_location = geolocator.geocode("Company Location, Brazil")
    if customer_location and company_location:
        return geodesic((customer_location.latitude, customer_location.longitude), (company_location.latitude, company_location.longitude)).kilometers
    else:
        return 0

def calculate_installation(module_quantity, inverter_quantity, customer_city):
    """
    Function to calculate the total installation costs.

    Args:
        module_quantity (int): The quantity of modules required.
        inverter_quantity (int): The quantity of inverters required.
        customer_city (str): The city where the installation will take place.

    Returns:
        float: The total installation costs.
    """
    distance = calculate_distance(customer_city)
    travel_expenses = cost_km * distance * 2
    lodging_expenses = hotel_per_person * math.ceil((inverter_quantity + module_quantity) / 3)
    food_expenses = food_per_person * math.ceil((inverter_quantity + module_quantity) / 3)
    man_hours = 8 * (inverter_quantity + module_quantity)
    man_hour_expenses = cost_hour_man * man_hours
    total_costs = travel_expenses + lodging_expenses + food_expenses + man_hour_expenses
    return total_costs

def calculate_equipment_price(module_power, inverter_power, roof_type):
    """
    Function to calculate the equipment price.

    Args:
        module_power (int): Power of each module in watts.
        inverter_power (float): Inverter power in kW.
        roof_type (str): The type of roof for installation.

    Returns:
        float: The equipment price.
    """
    module_price = 0.70 * module_power
    inverter_price = 0.80 * inverter_power * 1000
    roof_price = {
        "Brasilite": 100,
        "Aluzinc": 120,
        "Ceramic": 200,
        "Ground": 300,
        "Slab": 180
    }
    return module_price + inverter_price + roof_price.get(roof_type, 0)

def calculate_budget(total_installation_costs, equipment_price, module_quantity):
    """
    Function to calculate the budget.

    Args:
        total_installation_costs (float): The total installation costs.
        equipment_price (float): The equipment price.
        module_quantity (int): The quantity of modules required.

    Returns:
        float: The budget.
    """
    return total_installation_costs + equipment_price * module_quantity

def generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, orientation, module_power):
    """
    Generates a solar energy proposal based on customer information and project details.

    Parameters:
        customer_name (str): The name of the customer.
        customer_city (str): The city where the installation will take place.
        energy_consumption_average (int): The average energy consumption per month in kWh.
        phase (str): The main phase at the establishment (single-phase, biphasic, or three-phase).
        roof_type (str): The type of roof for installation.
        orientation (str): The orientation of the solar panels.
        module_power (int): The power of each solar module in watts.
    """
    current_date = datetime.date.today()
    irradiation = determine_irradiation(orientation)
    required_power = calculate_required_power(energy_consumption_average, irradiation)
    module_quantity = determine_module_quantity(energy_consumption_average, irradiation, module_power)
    total_power = calculate_total_power(module_quantity, module_power)
    average_monthly_generation, percentage = get_average_monthly_generation(total_power, irradiation, energy_consumption_average)
    inverter_power = calculate_inverter_power(total_power)
    inverter_phase = determine_inverter_phase(inverter_power)
    inverter_quantity = determine_inverter_quantity(phase, inverter_power)

    # Calculate the total installation costs
    total_installation_costs = calculate_installation(module_quantity, inverter_quantity, customer_city)

    # Calculate the equipment price
    equipment_price = calculate_equipment_price(module_power, inverter_power, roof_type)

    # Calculate the budget
    budget = calculate_budget(total_installation_costs, equipment_price, module_quantity)

    distance = calculate_distance(customer_city)
    cost_per_module = budget / module_quantity

    # Create a new window for the proposal
    proposal_window = tk.Toplevel()
    proposal_window.title("Solar Energy Proposal")

    # ARTEC - Solar Energy Proposal
    tk.Label(proposal_window, text="ARTEC - Solar Energy Proposal", font=("bold", 14)).grid(row=0, columnspan=2)

    # Customer information
    tk.Label(proposal_window, text="Customer Name:").grid(row=1, column=0, sticky="w")
    tk.Label(proposal_window, text=customer_name).grid(row=1, column=1, sticky="w")
    tk.Label(proposal_window, text="Customer City:").grid(row=2, column=0, sticky="w")
    tk.Label(proposal_window, text=customer_city).grid(row=2, column=1, sticky="w")
    tk.Label(proposal_window, text="Energy Consumption (kWh/month):").grid(row=3, column=0, sticky="w")
    tk.Label(proposal_window, text=energy_consumption_average).grid(row=3, column=1, sticky="w")
    tk.Label(proposal_window, text="Phase:").grid(row=4, column=0, sticky="w")
    tk.Label(proposal_window, text=phase).grid(row=4, column=1, sticky="w")
    tk.Label(proposal_window, text="Roof Type:").grid(row=5, column=0, sticky="w")
    tk.Label(proposal_window, text=roof_type).grid(row=5, column=1, sticky="w")
    tk.Label(proposal_window, text="Orientation:").grid(row=6, column=0, sticky="w")
    tk.Label(proposal_window, text=orientation).grid(row=6, column=1, sticky="w")
    tk.Label(proposal_window, text="Module Power (W):").grid(row=7, column=0, sticky="w")
    tk.Label(proposal_window, text=module_power).grid(row=7, column=1, sticky="w")

    # Display proposal details
    tk.Label(proposal_window, text="System Description", font=("bold", 14)).grid(row=8, columnspan=2)
    tk.Label(proposal_window, text="Total System Power (kWp):").grid(row=9, column=0, sticky="w")
    tk.Label(proposal_window, text=f"{total_power:.2f}").grid(row=9, column=1, sticky="w")
    tk.Label(proposal_window, text="Module Quantity:").grid(row=10, column=0, sticky="w")
    tk.Label(proposal_window, text=module_quantity).grid(row=10, column=1, sticky="w")
    tk.Label(proposal_window, text="Inverter Quantity:").grid(row=11, column=0, sticky="w")
    tk.Label(proposal_window, text=inverter_quantity).grid(row=11, column=1, sticky="w")
    tk.Label(proposal_window, text="Structure Material:").grid(row=12, column=0, sticky="w")
    tk.Label(proposal_window, text="To be filled").grid(row=12, column=1, sticky="w")  # Placeholder for structure material
    tk.Label(proposal_window, text="Average Monthly Generation (kWh/month):").grid(row=13, column=0, sticky="w")
    tk.Label(proposal_window, text=f"{average_monthly_generation:.2f}").grid(row=13, column=1, sticky="w")
    tk.Label(proposal_window, text="Surplus Percentage:").grid(row=14, column=0, sticky="w")
    tk.Label(proposal_window, text=f"{percentage:.2f}%").grid(row=14, column=1, sticky="w")

    tk.Label(proposal_window, text="Cost Information", font=("bold", 14)).grid(row=15, columnspan=2)
    tk.Label(proposal_window, text="Total Project Price ($):").grid(row=16, column=0, sticky="w")
    tk.Label(proposal_window, text=f"${budget:,.2f}").grid(row=16, column=1, sticky="w")
    tk.Label(proposal_window, text="Installation Cost per Module ($):").grid(row=17, column=0, sticky="w")
    tk.Label(proposal_window, text=f"${cost_per_module:,.2f}").grid(row=17, column=1, sticky="w")
    tk.Label(proposal_window, text="Validity of the Proposal:").grid(row=18, column=0, sticky="w")
    tk.Label(proposal_window, text=current_date + datetime.timedelta(days=5)).grid(row=18, column=1, sticky="w")

    tk.Button(proposal_window, text="Close", command=proposal_window.destroy).grid(row=19, columnspan=2)

if __name__ == "__main__":
    main()
