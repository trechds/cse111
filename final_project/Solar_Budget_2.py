import datetime

def main():
    print("Welcome to the Solar Budget of AR-TEC")
    print("This program will calculate your energy consumption and generate a Solar Energy Generation Proposal for your house, commerce, or industry.")
    print("Let's get started!\n")

    # Ask for user inputs
    customer_name = input("Enter the customer's name: ")
    customer_city = input("Enter the customer's city-state: ")
    energy_consumption_average = int(input("On average, how much energy do you consume per month? (kWh): "))

    phase = get_phase()
    roof_type = get_roof_type()

    orientation = input("Select the orientation the panels will be installed: ").capitalize()

    module_power = int(input("Please select the Module Power you want (Watts): "))

    generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, orientation, module_power)

def get_phase():
    phases = ["Single-phase", "Biphasic", "Three-phase"]
    while True:
        phase = input("Please select the main phase at your establishment (Single-phase/Biphasic/Three-phase): ").capitalize()
        if phase in phases:
            return phase

def get_roof_type():
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
            return roof_type

def determine_irradiation(orientation):
    orientation_irradiation = {
        "North": 112, "Northeast": 110, "Northwest": 110,
        "East": 104, "West": 104, "South": 95,
        "Southeast": 100, "Southwest": 100
    }
    return orientation_irradiation[orientation]

def calculate_required_power(energy_consumption_average, irradiation):
    required_power = energy_consumption_average / irradiation
    return required_power

def determine_module_quantity(energy_consumption_average, irradiation, module_power):
    module_quantity = ((energy_consumption_average + energy_consumption_average * 0.3) / irradiation) * 1000 / module_power
    return int(module_quantity + 0.99)  # Round up to the nearest integer

def calculate_total_power(module_quantity, module_power):
    total_power = (module_quantity * module_power) / 1000
    return total_power

def get_average_monthly_generation(total_power, irradiation):
    average_monthly_generation = total_power * irradiation
    return average_monthly_generation

def calculate_inverter_power(total_power):
    overload = 0.3
    inverter_power = total_power - overload
    power_inverters = [0.6, 1, 1.3, 1.6, 2, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 33, 35, 40, 45, 50, 60, 75, 100]
    return min(power_inverters, key=lambda x: abs(x - inverter_power))

def determine_inverter_phase(inverter_power):
    if inverter_power <= 2:
        return "Micro-inverter"
    elif inverter_power <= 12:
        return "Single-phase"
    else:
        return "Three-phase"

def determine_inverter_quantity(phase):
    if phase == "Single-phase":
        return 1
    elif phase == "Biphasic":
        return 2
    else:
        return 1 if phase == "Three-phase" else 0

def calculate_budget(module_quantity, module_power, total_power, inverter_power, phase, roof_type):
    modules_price = {
        550: 1600, 500: 1400, 450: 1200, 400: 1000, 350: 800, 300: 600
    }
    inverters_price = {
        0.6: 600, 1: 1000, 1.3: 1500, 1.6: 1600, 2: 3200, 4: 4000, 5: 5000, 6: 6000,
        7: 7000, 8: 8000, 10: 10000, 12: 12000, 15: 15000, 20: 20000, 25: 25000,
        30: 30000, 33: 33000, 35: 35000, 40: 40000, 45: 45000, 50: 50000, 60: 60000,
        75: 75000, 100: 100000
    }
    roof_types_price = {
        "Brasilite": 30, "Aluzinc": 45, "Ceramic": 130, "Ground": 120, "Slab": 150
    }

    module_price = modules_price[module_power]
    inverter_price = inverters_price[inverter_power]
    roof_type_price = roof_types_price[roof_type]

    installation_cost = calculate_installation(module_quantity)
    total_price = (module_quantity * module_price) + (inverter_price * determine_inverter_quantity(phase)) + roof_type_price + installation_cost
    return total_price

def generate_proposal(customer_name, customer_city, energy_consumption_average, phase, roof_type, orientation, module_power):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    irradiation = determine_irradiation(orientation)
    required_power = calculate_required_power(energy_consumption_average, irradiation)
    module_quantity = determine_module_quantity(energy_consumption_average, irradiation, module_power)
    total_power = calculate_total_power(module_quantity, module_power)
    average_monthly_generation = get_average_monthly_generation(total_power, irradiation)
    inverter_power = calculate_inverter_power(total_power)
    inverter_phase = determine_inverter_phase(inverter_power)
    budget = calculate_budget(module_quantity, module_power, total_power, inverter_power, phase, roof_type)

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
    print(f"Inverter Power: {inverter_power:.2f} kW")
    print(f"Structure Material: {roof_type} for ({orientation})")
    print(f"Average Monthly Energy Generation: {average_monthly_generation:.2f} kWh/month\n")
    print(f"You will have an average surplus of {(average_monthly_generation - energy_consumption_average) / energy_consumption_average * 100:.2f}% every month\n")
    print(f"Total Project Price: $ {budget:.2f}")
    print(f"Installation Cost per Module: $ {(budget - module_quantity * module_price) / module_quantity:.2f}")
    print(f"Validity of the Proposal: {current_date + datetime.timedelta(days=5)}\n")
    print("For more information, please contact Thiago Rech: +5554991424628")
    print("Thank you for your attention!")

if __name__ == "__main__":
    main()
