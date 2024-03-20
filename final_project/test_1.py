import math

def main():
    customer_info = get_customer_info()
    roof_type = determine_roof_type()
    panel_orientation = determine_panel_orientation()
    energy_consumption = calculate_energy_consumption()
    total_power = calculate_total_power()
    average_monthly_generation = calculate_average_monthly_generation(total_power, panel_orientation)
    inverter_power = calculate_inverter_power(total_power)
    inverter_type = determine_inverter_type(inverter_power)
    inverter_quantity = calculate_inverter_quantity(total_power)
    roof_price = get_roof_type(roof_type)
    energy_company = get_energy_company()
    budget = calculate_budget(total_power, inverter_quantity, roof_price)

    generate_proposal(customer_info, roof_type, panel_orientation, energy_consumption, average_monthly_generation,
                      inverter_power, inverter_type, inverter_quantity, roof_price, energy_company, budget)

def get_customer_info():
    customer_name = input("Enter the customer's full name: ")
    phone_number = input("Enter the customer's phone number: ")
    email = input("Enter the customer's email: ")
    city_state = input("Enter the customer's city-state: ")
    seller_name = input("Enter the seller's name: ")
    mains_phase = input("Select the mains phase: ")
    energy_company = get_energy_company()
    return {"customer_name": customer_name, "phone_number": phone_number, "email": email, "city_state": city_state,
            "seller_name": seller_name, "mains_phase": mains_phase, "energy_company": energy_company}

def determine_roof_type():
    roof_type = input("Select the type of roof (Brasilite, Aluzinc, Ceramic, Ground, Slab): ")
    return roof_type

def determine_panel_orientation():
    orientations = ["North", "Northeast", "Northwest", "East", "West", "South", "Southeast", "Southwest"]
    panel_orientation = input("Select the orientation of the solar panels: ").capitalize()
    if panel_orientation not in orientations:
        print("Invalid orientation selected.")
        return determine_panel_orientation()
    return panel_orientation

def calculate_energy_consumption():
    consumption_option = input("Do you want to enter your own average consumption or calculate it? (1 or 2): ")
    if consumption_option == "1":
        energy_consumption_average = float(input("Enter your energy consumption average in kWh: "))
    elif consumption_option == "2":
        months_consumption = []
        for month in range(1, 13):
            consumption = input(f"Enter consumption for month {month} (press enter if none): ")
            if consumption:
                months_consumption.append(float(consumption))
        energy_consumption_average = sum(months_consumption) / len(months_consumption)
    else:
        print("Invalid option selected.")
        return calculate_energy_consumption()
    return energy_consumption_average

def calculate_total_power():
    module_quantity = int(input("Enter the quantity of solar panels: "))
    module_power = float(input("Enter the power rating of each solar panel (in watts): "))
    total_power = module_quantity * module_power / 1000  # Convert to kW
    return total_power

def calculate_average_monthly_generation(total_power, panel_orientation):
    irradiation = get_irradiation(panel_orientation)
    average_monthly_generation = total_power * irradiation
    return average_monthly_generation

def calculate_inverter_power(total_power):
    overload = 0.3  # 30% overload
    inverter_power = total_power / (1 - overload)
    rounded_powers = [0.6, 1, 1.3, 1.6, 2, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 33, 35, 40, 45, 50, 60, 75, 100]
    inverter_power = min(rounded_powers, key=lambda x: abs(x - inverter_power))
    return inverter_power

def determine_inverter_type(inverter_power):
    if inverter_power <= 2:
        return "Micro-inverter"
    elif inverter_power <= 12:
        return "Single-phase"
    else:
        return "Three-phase"

def calculate_inverter_quantity(total_power):
    return math.ceil(total_power / 30)  # Assuming each inverter has a power rating of 30 kW

def get_roof_type(roof_type):
    roof_types = {
        "Brasilite": {"structure_type": "Mini Rail 24cm", "price_per_module": 30},
        "Aluzinc": {"structure_type": "Mini Rail 40cm", "price_per_module": 45},
        "Ceramic": {"structure_type": "Colonial", "price_per_module": 130},
        "Ground": {"structure_type": "Block", "price_per_module": 120},
        "Slab": {"structure_type": "Steel", "price_per_module": 150}
    }
    return roof_types.get(roof_type, {"structure_type": "Unknown", "price_per_module": 0})

def get_energy_company():
    energy_companies = ["CPFL", "RGE", "Coprel", "Cerfox"]
    return input("Enter the Energy Company (CPFL, RGE, Coprel, Cerfox): ").upper()

def calculate_budget(total_power, inverter_quantity, roof_price):
    module_price = roof_price["price_per_module"]
    total_cost = total_power * module_price + inverter_quantity * 5000  # Assuming $5000 per inverter
    return total_cost

def generate_proposal(customer_info, roof_type, panel_orientation, energy_consumption, average_monthly_generation,
                      inverter_power, inverter_type, inverter_quantity, roof_price, energy_company, budget):
    print("----- Solar Energy Proposal -----")
    print(f"Customer Name: {customer_info['customer_name']}")
    print(f"Phone Number: {customer_info['phone_number']}")
    print(f"Email: {customer_info['email']}")
    print(f"City-State: {customer_info['city_state']}")
    print(f"Seller Name: {customer_info['seller_name']}")
    print(f"Mains Phase: {customer_info['mains_phase']}")
    print(f"Energy Company: {energy_company}")
    print(f"Roof Type: {roof_type}")
    print(f"Panel Orientation: {panel_orientation}")
    print(f"Energy Consumption (kWh): {energy_consumption}")
    print(f"Average Monthly Generation (kWh): {average_monthly_generation}")
    print(f"Inverter Power (kW): {inverter_power}")
    print(f"Inverter Type: {inverter_type}")
    print(f"Inverter Quantity: {inverter_quantity}")
    print(f"Roof Price: {roof_price['price_per_module']()}/module")
    print(f"Total Cost ($): {budget}")
    print("\nPlease review all information above and confirm your order by calling or emailing us.")
    
    