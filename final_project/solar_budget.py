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
    Main function to interact with the user and generate a solar energy proposal.
    """
    print("Welcome to the Solar Budget of AR-TEC")
    print("This program will calculate your energy consumption and generate a Solar Energy Generation Proposal for your house, commerce, or industry.")
    print("Let's get started!\n")
    # Customer information
    customer_name = input("Enter the customer's name: ")
    customer_city = input("Enter the customer's city-state: ")
    # Energy consumption
    while True:
        try:
            energy_consumption_average = int(input("On average, how much energy do you consume per month? (kWh): "))
            break
        except ValueError:
            print("Please enter a valid integer for energy consumption.")
    # Main phase selection
    phase = get_phase()
    # Roof type selection
    roof_type, structure_material = get_roof_type()
    # Panel orientation selection
    orientation = get_orientation()
    # Module power selection
    module_power = get_module_power()
    # Generate proposal
    generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, structure_material, orientation, module_power)

def get_phase():
    """
    Function to get the main phase at the establishment.

    Returns:
        str: The selected phase.
    """
    phases = ["Single-phase", "Biphasic", "Three-phase"]
    while True:
        phase = input("Please select the main phase at your establishment (Single-phase/Biphasic/Three-phase): ").capitalize()
        if phase in phases:
            return phase
        else:
            print("Invalid phase. Please choose from the available options.")

def get_roof_type():
    """
    Function to select the panel installation structure.

    Returns:
        tuple: A tuple containing the selected roof type and its structure material.
    """
    roof_types = {
        "Brasilite": {"structure_type": "Mini Rail 24cm", "price_per_module": 30},
        "Aluzinc": {"structure_type": "Mini Rail 40cm", "price_per_module": 45},
        "Ceramic": {"structure_type": "Colonial", "price_per_module": 130},
        "Ground": {"structure_type": "Block", "price_per_module": 120},
        "Slab": {"structure_type": "Steel", "price_per_module": 150}
    }
    while True:
        roof_type = input("Select the panel installation structure (Brasilite/Aluzinc/Ceramic/Ground/Slab): ").capitalize()
        if roof_type in roof_types:
            return roof_type, roof_types[roof_type]["structure_type"]
        else:
            print("Invalid roof type. Please choose from the available options.")

def get_orientation():
    """
    Function to select the panel orientation.

    Returns:
        str: The selected panel orientation.
    """
    orientations = ["North", "Northeast", "Northwest", "East", "West", "South", "Southeast", "Southwest"]
    while True:
        orientation = input("Select the orientation the panels will be installed (North/Northeast/Northwest/East/West/South/Southeast/Southwest): ").capitalize()
        if orientation in orientations:
            return orientation
        else:
            print("Invalid orientation. Please choose from the available options.")

def get_module_power():
    """
    Function to select the module power.

    Returns:
        int: The selected module power in watts.
    """
    module_options = [550, 500, 450, 400, 350, 300]
    while True:
        try:
            module_power = int(input(f"Please select the Module Power in 'Watts', that you want ({', '.join(map(str, module_options))}): "))
            if module_power in module_options:
                return module_power
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid integer for module power.")

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
    if inverter_power <= 2:
        return "Micro-inverter"
    elif inverter_power <= 12:
        return "Single-phase"
    else:
        return "Three-phase"

def determine_inverter_quantity(phase, inverter_power):
    """
    Function to determine the inverter quantity.

    Args:
        phase (str): The phase of the inverter.
        inverter_power (float): Inverter power in kW.

    Returns:
        int: The quantity of inverters required.
    """
    if phase == "Single-phase":
        return 1 if inverter_power <= 12 else 3
    elif phase == "Biphasic":
        return 2
    else:
        return 1

def calculate_distance(customer_city):
    """
    Function to calculate the distance between the customer's city and Marau-RS (The city where the Company is located).

    Args:
        customer_city (str): The city where the customer is located.

    Returns:
        float: The distance between the customer's city and Marau-RS in kilometers.
    """
    # Location for Marau-RS
    marau_location = (-28.4481, -52.1996)

    # Inicialize o geolocalizador do Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Obtenha as coordenadas da cidade do cliente
    customer_location = geolocator.geocode(customer_city)

    # Verifique se a cidade foi encontrada
    if customer_location:
        customer_coords = (customer_location.latitude, customer_location.longitude)
    else:
        print(f"We didn't find your location")
        return None

    # Calcula a distância entre Marau-RS e a cidade do cliente
    distance = geodesic(marau_location, customer_coords).kilometers

    return distance

def calculate_installation(module_quantity, inverter_quantity, customer_city):
    """
    Calculates the total installation costs based on the number of modules, inverters, and the customer's city.

    Parameters:
        module_quantity (int): The quantity of solar modules required.
        inverter_quantity (int): The quantity of inverters required.
        customer_city (str): The city where the installation will take place.

    Returns:
        float: The total installation costs.
    """
    # Determine the number of employees based on the number of modules
    if module_quantity <= 10:
        employee_qnty = 2
    elif module_quantity <= 30:
        employee_qnty = 3
    elif module_quantity <= 50:
        employee_qnty = 4
    elif module_quantity <= 100:
        employee_qnty = 5
    else:
        employee_qnty = 6

    # Calculate travel distance and cost
    distance = calculate_distance(customer_city)
    displacement = distance * 2
    trips_qnty = module_quantity // 10  # Every 10 modules, a displacement is required
    displacement_cost = (displacement * trips_qnty) * cost_km

    # Calculate working and commuting time
    hour_man = (module_quantity / 20 * 8) + (inverter_quantity * 4)
    work_time = hour_man / employee_qnty
    displacement_time = (displacement / 60) * 2 * trips_qnty
    total_time = work_time + displacement_time
    total_days = total_time / 8

    labor_price = hour_man * cost_hour_man * employee_qnty
    food_cost = food_per_person * employee_qnty

    # Determine travel and hotel prices
    travel_price = get_travel_price(module_quantity, inverter_quantity, distance, total_days)
    hotel_price = get_hotel_price(module_quantity, inverter_quantity, distance, total_days)
    
    # Determine the lowest price between travel and hotel expenses
    extra_expenses = determine_travel_hotel(travel_price, hotel_price)

    # Calculate the total installation cost
    total_installation_costs = labor_price + food_cost + extra_expenses + displacement_cost

    return total_installation_costs

def get_travel_price(module_quantity, inverter_quantity, distance, total_days):
    """
    Calculates the travel expenses for the installation team based on the number of modules, inverters, travel distance, and total working days.

    Parameters:
        module_quantity (int): The quantity of solar modules required.
        inverter_quantity (int): The quantity of inverters required.
        distance (float): The distance between the customer's city and Marau-RS.
        total_days (int): The total number of working days required for installation.

    Returns:
        float: The total travel expenses.
    """
    # Determine the number of employees based on the number of modules
    if module_quantity <= 10:
        employee_qnty = 2
    elif module_quantity <= 30:
        employee_qnty = 3
    elif module_quantity <= 50:
        employee_qnty = 4
    elif module_quantity <= 100:
        employee_qnty = 5
    else:
        employee_qnty = 6

    # Calculate travel distance and cost
    gas = distance * cost_km * 2 * total_days
    displacement_labor = distance * 2 / 60 * 2 * total_days * cost_hour_man * employee_qnty
    cost_food = food_per_person * employee_qnty * (module_quantity // 10)

    # Calculate travel price
    travel_price = gas + displacement_labor + cost_food
    return travel_price

def get_hotel_price(module_quantity, inverter_quantity, distance, total_days):
    """
    Calculates the hotel expenses for the installation team based on the number of modules, inverters, travel distance, and total working days.

    Parameters:
        module_quantity (int): The quantity of solar modules required.
        inverter_quantity (int): The quantity of inverters required.
        distance (float): The distance between the customer's city and Marau-RS.
        total_days (int): The total number of working days required for installation.

    Returns:
        float: The total hotel expenses.
    """
    # Determine the number of employees based on the number of modules
    if module_quantity <= 10:
        employee_qnty = 2
    elif module_quantity <= 30:
        employee_qnty = 3
    elif module_quantity <= 50:
        employee_qnty = 4
    elif module_quantity <= 100:
        employee_qnty = 5
    else:
        employee_qnty = 6

    # Calculate travel distance and cost
    gas = distance * cost_km * 2
    displacement_labor = (distance * 2 / 60 * 2) / (module_quantity // 10) * cost_hour_man * employee_qnty
    cost_food = food_per_person * employee_qnty * (module_quantity // 10) * 2
    hotel_cost = (module_quantity // 10 - 1) * employee_qnty * hotel_per_person

    # Calculate hotel price
    hotel_price = gas + displacement_labor + cost_food + hotel_cost
    return hotel_price

def determine_travel_hotel(travel_price, hotel_price):
    """
    Determines the lower cost between travel expenses and hotel expenses.

    Parameters:
        travel_price (float): The total travel expenses.
        hotel_price (float): The total hotel expenses.

    Returns:
        float: The lower of the two expenses.
    """
    extra_expenses = 0
    if travel_price < hotel_price:
        extra_expenses = travel_price
    else:
        extra_expenses = hotel_price

    return extra_expenses

def calculate_equipment_price(module_power, inverter_power, roof_type):
    """
    Calculates the total price of equipment (solar modules, inverters, and structure) based on their respective powers and roof type.

    Parameters:
        module_power (int): The power of each solar module in watts.
        inverter_power (float): The power of each inverter in kW.
        roof_type (str): The type of roof for installation.

    Returns:
        float: The total price of equipment.
    """
    modules_prices = {
        "550W": 1600,
        "500W": 1400,
        "450W": 1200,
        "400W": 1000,
        "350W": 800,
        "300W": 600
    }
    inverters_prices = {
        0.6: 600,
        1: 1000,
        1.3: 1500,
        1.6: 1600,
        2: 3200,
        4: 4000,
        5: 5000,
        6: 6000,
        7: 7000,
        8: 8000,
        10: 10000,
        12: 12000,
        15: 15000,
        20: 20000,
        25: 25000,
        30: 30000,
        33: 33000,
        35: 35000,
        40: 40000,
        45: 45000,
        50: 50000,
        60: 60000,
        75: 75000,
        100: 100000
    }
    roof_types = {
        "Brasilite": {"structure_type": "Mini Rail 24cm", "price_per_module": 30},
        "Aluzinc": {"structure_type": "Mini Rail 40cm", "price_per_module": 45},
        "Ceramic": {"structure_type": "Colonial", "price_per_module": 130},
        "Ground": {"structure_type": "Block", "price_per_module": 120},
        "Slab": {"structure_type": "Steel", "price_per_module": 150}
    }
    
    module_price = modules_prices.get(f"{module_power}W", 0)
    inverter_price = inverters_prices.get(inverter_power, 0)
    structure_price = roof_types.get(roof_type, {}).get("price_per_module", 0)

    modules_cost = module_power * module_price
    inverter_cost = inverter_power * inverter_price

    equipment_price = modules_cost + inverter_cost + structure_price

    return equipment_price

def calculate_budget(total_installation_costs, equipment_price, module_quantity):
    """
    Calculates the total budget required for the solar energy project based on installation costs, equipment price, and the quantity of modules.

    Parameters:
        total_installation_costs (float): The total installation costs.
        equipment_price (float): The total price of equipment.
        module_quantity (int): The quantity of solar modules required.

    Returns:
        float: The total budget for the project.
    """
    budget = total_installation_costs + equipment_price
    cost_per_module = budget / module_quantity
    return budget

def generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, structure_material, orientation, module_power):
    """
    Generates a solar energy proposal based on customer information and project details.

    Parameters:
        customer_name (str): The name of the customer.
        customer_city (str): The city where the installation will take place.
        energy_consumption_average (int): The average energy consumption per month in kWh.
        phase (str): The main phase at the establishment (single-phase, biphasic, or three-phase).
        roof_type (str): The type of roof for installation.
        structure_material (str): The material of the installation structure.
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

    print()
    print("ARTEC - Solar Energy Proposal")
    print("--------------------------------------")
    print(f"Customer Name: {customer_name}")
    print(f"City: {customer_city}")
    print(f"Distance: {distance:.2f}")
    print(f"Energy Consumption: {energy_consumption_average} kWh/month")
    print(f"Required Power: {required_power:.2f} kWp")
    print(f"Date: {current_date}\n")

    print("The purpose of this proposal is to install a solar energy system for your home or business,")
    print("providing you with renewable and sustainable energy sources. Our team will be composed of highly trained professionals.\n")

    print("System Description:\n")
    print(f"Total System Power: {total_power:.2f} kWp")
    print(f"Modules: {module_quantity} modules of {module_power} W")
    print(f"Inverter: {inverter_quantity} {inverter_phase} inverter of {inverter_power} kW")
    print(f"Structure Material: {structure_material} for {roof_type}")
    print(f"Average Monthly Energy Generation: {average_monthly_generation:.2f} kWh/month")
    print(f"You will have an average surplus of {percentage:.2f}% every month\n")
    print(f"Total Project Price: $ {budget:,.2f}")
    print(f"Installation Cost per Module: $ {cost_per_module:,.2f}")
    print(f"Validity of the Proposal: {current_date + datetime.timedelta(days=5)}\n")
    print("For more information, please contact Thiago Rech: +5554991424628")
    print("Thank you for your attention!")

if __name__ == "__main__":
    main()