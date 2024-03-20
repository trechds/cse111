import datetime
import math

def main():
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
    roof_type = get_roof_type()

    # Panel orientation selection
    orientation = input("Select the orientation the panels will be installed: ").capitalize()

    # Module power selection
    while True:
        try:
            module_power = int(input("Please select the Module Power you want (Watts): "))
            break
        except ValueError:
            print("Please enter a valid integer for module power.")

    # Generate proposal
    generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, orientation, module_power)

def get_phase():
    phases = ["Single-phase", "Biphasic", "Three-phase"]
    while True:
        phase = input("Please select the main phase at your establishment (Single-phase/Biphasic/Three-phase): ").capitalize()
        if phase in phases:
            return phase
        else:
            print("Invalid phase. Please choose from the available options.")

def get_roof_type():
    roof_types = {
        "Brasilite": {"structure_type": "Mini Rail 24cm", "price_per_module": 30},
        "Aluzinc": {"structure_type": "Mini Rail 40cm", "price_per_module": 45},
        "Ceramic": {"structure_type": "Colonial", "price_per_module": 130},
        "Ground": {"structure_type": "Block", "price_per_module": 120},
        "Slab": {"structure_type": "Steel", "price_per_module": 150},
    }
    while True:
        roof_type = input("Select the panel installation structure (Brasilite/Aluzinc/Ceramic/Ground/Slab): ").capitalize()
        if roof_type in roof_types:
            return roof_types[roof_type]
        else:
            print("Invalid roof type. Please choose from the available options.")

def determine_irradiation(orientation):
    orientation_irradiation = {
        "North": 112,
        "Northeast": 110,
        "Northwest": 110,
        "East": 104,
        "West": 104,
        "South": 95,
        "Southeast": 100,
        "Southwest": 100,
    }
    return orientation_irradiation.get(orientation, 0)

def calculate_required_power(energy_consumption_average, irradiation):
    return energy_consumption_average / irradiation

def determine_module_quantity(energy_consumption_average, irradiation, module_power):
    module_quantity = math.ceil((energy_consumption_average * 1.3) / irradiation * 1000 / module_power)
    return module_quantity

def calculate_total_power(module_quantity, module_power):
    return module_quantity * module_power / 1000

def get_average_monthly_generation(total_power, irradiation):
    return total_power * irradiation * 12

def calculate_inverter_power(total_power):
    overload = 0.30
    inverter_power = total_power / (1 + overload)
    power_inverters = [0.6, 1, 1.3, 1.6, 2, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 33, 35, 40, 45, 50, 60, 75, 100]
    return min(power_inverters, key=lambda x:abs(x-inverter_power))

def determine_inverter_phase(inverter_power):
    if inverter_power <= 2:
        return "Micro-inverter"
    elif inverter_power <= 12:
        return "Single-phase"
    else:
        return "Three-phase"

def determine_inverter_quantity(phase, inverter_power):
    if phase == "Single-phase":
        return 1 if inverter_power <= 12 else 3
    elif phase == "Biphasic":
        return 2
    else:
        return 1

def calculate_installation(module_quantity, roof_type):
    # Placeholder function, actual implementation needed
    installation_cost_per_module = roof_type["price_per_module"]
    return module_quantity * installation_cost_per_module

def determine_travel_hotel(travel=True):
    # Placeholder function, actual implementation needed
    return 500

def calculate_budget(module_quantity, module_power, total_power, inverter_power, phase, roof_type, orientation):
    installation_cost = calculate_installation(module_quantity, roof_type)
    travel_hotel_cost = determine_travel_hotel()
    material_cost = module_quantity * module_power
    inverter_cost = inverter_power * 100
    labor_cost = material_cost * 0.1
    overhead_cost = labor_cost * 0.1
    profit_margin = overhead_cost * 0.2

    average_monthly_generation = get_average_monthly_generation(total_power, determine_irradiation(orientation))
    monthly_savings = (energy_consumption_average / 12) - average_monthly_generation
    annual_savings = monthly_savings * 12
    system_lifetime = 25  # years
    total_savings = annual_savings * system_lifetime

    return installation_cost + travel_hotel_cost + material_cost + inverter_cost + labor_cost + overhead_cost + profit_margin, total_savings

def generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, orientation, module_power):
    current_date = datetime.date.today()
    irradiation = determine_irradiation(orientation)
    required_power = calculate_required_power(energy_consumption_average, irradiation)
    module_quantity = determine_module_quantity(energy_consumption_average, irradiation, module_power)
    total_power = calculate_total_power(module_quantity, module_power)
    average_monthly_generation = get_average_monthly_generation(total_power, irradiation)
    inverter_power = calculate_inverter_power(total_power)
    inverter_phase = determine_inverter_phase(inverter_power)
    inverter_quantity = determine_inverter_quantity(phase, inverter_power)
    budget, total_savings = calculate_budget(module_quantity, module_power, total_power, inverter_power, phase, roof_type, orientation)

    print("ARTEC - Solar Energy Proposal")
    print("--------------------------------------")
    print(f"Customer Name: {customer_name}")
    print(f"City: {customer_city}")
    print(f"Energy Consumption: {energy_consumption_average} kWh/month")
    print(f"Required Power: {required_power:.2f} kWp")
    print(f"Date: {current_date}\n")

    print("The purpose of this proposal is to install a solar energy system for your home or business,")
    print("providing you with renewable and sustainable energy sources. Our team will be composed of highly trained professionals.\n")
    print("System Description:\n")
    print(f"Total System Power: {total_power:.2f} kWp")
    print(f"Modules Quantity: {module_quantity}")
    print(f"Modules Power: {module_power} W")
    print(f"Inverter Type: {inverter_phase}")
    print(f"Inverter Power: {inverter_power} kW")
    print(f"Structure Material: {roof_type['structure_type']} ({roof_type['price_per_module']}$/module)")
    print(f"Average Monthly Energy Generation: {average_monthly_generation:.2f} kWh/month")
    print(f"Average Monthly Savings: {monthly_savings:.2f} kWh/month")
    print(f"Total Project Price: $ {budget:.2f}")
    print(f"Total Savings: $ {total_savings:.2f}")
    print(f"Installation Cost per Module: $ {calculate_installation(module_quantity, roof_type) / module_quantity:.2f}")
    print(f"Validity of the Proposal: {current_date + datetime.timedelta(days=5)}\n")
    print("For more information, please contact Thiago Rech: +5554991424628")
    print("Thank you for your attention!")

if __name__ == "__main__":
    main()