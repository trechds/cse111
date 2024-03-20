def water_column_height(tower_height, tank_height):
    """
    Calculate the height of a water column in a distribution system.
    Args:
    - tower_height (float): Height of the tower in meters.
    - tank_height (float): Height of the tank walls on top of the tower in meters.
    Returns:
    float: Height of the water column in the distribution system.
    """
    # h = t + (3w) / 4
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity on a water column.
    Args:
    - height (float): Height of the water column in meters.
    Returns:
    float: Pressure in kilopascals.
    """
    # P = (ρgh) / 1000
    density_of_water = 998.2  # kg/m^3
    gravity_acceleration = 9.80665  # m/s^2
    pressure = (density_of_water * gravity_acceleration * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the water pressure lost due to friction within a pipe.
    Args:
    - pipe_diameter (float): Diameter of the pipe in meters.
    - pipe_length (float): Length of the pipe in meters.
    - friction_factor (float): Friction factor of the pipe.
    - fluid_velocity (float): Velocity of water flowing through the pipe in meters/second.
    Returns:
    float: Pressure loss in kilopascals.
    """
    # P = (−fLρv²) / (2000d)
    density_of_water = 998.2  # kg/m^3
    pressure_loss = (-friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the water pressure lost due to fittings in a pipeline.
    Args:
    - fluid_velocity (float): Velocity of water flowing through the pipe in meters/second.
    - quantity_fittings (int): Quantity of fittings (e.g., bends) in the pipeline.
    Returns:
    float: Pressure loss in kilopascals.
    """
    # P = (−0.04ρv²n) / 2000
    density_of_water = 998.2  # kg/m^3
    pressure_loss = (-0.04 * density_of_water * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for water flowing through a pipe.
    Args:
    - hydraulic_diameter (float): Hydraulic diameter of the pipe in meters.
    - fluid_velocity (float): Velocity of water flowing through the pipe in meters/second.
    Returns:
    float: Reynolds number (unitless).
    """
    # R = (ρdv) / μ
    density_of_water = 998.2  # kg/m^3
    dynamic_viscosity = 0.0010016  # Pascal seconds
    reynolds = (density_of_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the water pressure lost due to a reduction in pipe diameter.
    Args:
    - larger_diameter (float): Diameter of the larger pipe in meters.
    - fluid_velocity (float): Velocity of water flowing through the larger diameter pipe in meters/second.
    - reynolds_number (float): Reynolds number corresponding to the larger diameter pipe.
    - smaller_diameter (float): Diameter of the smaller pipe in meters.
    Returns:
    float: Pressure loss in kilopascals.
    """
    # k = (0.1 + (50 / R)) ((D / d)^4 − 1)
    # P = (−kρv²) / 2000
    constant_k = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_loss = (-constant_k * density_of_water * fluid_velocity**2) / 2000
    return pressure_loss

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

density_of_water = 998.2  # kg/m^3

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
