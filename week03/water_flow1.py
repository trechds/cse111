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