import math

def main():
    can_sizes = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42},
    ]

    print("{:<15} {:<15} {:<15} {:<20} {:<20}".format("Can Name", "Volume", "Surface Area", "Storage Efficiency", "Cost Efficiency"))
    print("-" * 85)

    best_storage_efficiency = {"name": None, "value": 0}
    best_cost_efficiency = {"name": None, "value": 0}

    for can in can_sizes:
        volume = compute_volume(can["radius"], can["height"])
        surface_area = compute_surface_area(can["radius"], can["height"])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can["cost"])

        print("{:<15} {:<15.2f} {:<15.2f} {:<20.2f} {:<20.2f}".format(can["name"], volume, surface_area, storage_efficiency, cost_efficiency))

        # Update best storage efficiency
        if storage_efficiency > best_storage_efficiency["value"]:
            best_storage_efficiency["name"] = can["name"]
            best_storage_efficiency["value"] = storage_efficiency

        # Update best cost efficiency
        if cost_efficiency > best_cost_efficiency["value"]:
            best_cost_efficiency["name"] = can["name"]
            best_cost_efficiency["value"] = cost_efficiency

    print("\nBest Storage Efficiency: {} ({:.2f})".format(best_storage_efficiency["name"], best_storage_efficiency["value"]))
    print("Best Cost Efficiency: {} ({:.2f})".format(best_cost_efficiency["name"], best_cost_efficiency["value"]))

def compute_volume(radius, height):
    """Compute the volume of a cylinder."""
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    """Compute the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    """Compute the storage efficiency of a cylinder."""
    return volume / surface_area

def compute_cost_efficiency(volume, cost):
    """Compute the cost efficiency of a cylinder."""
    return volume / cost

if __name__ == "__main__":
    main()
