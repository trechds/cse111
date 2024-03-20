import math

list = [
    ['#1 Picnic', 6.83, 10.16, 0.28],
    ['#1 Tall', 7.78, 11.91, 0.43],
    ['#2', 8.73, 11.59, 0.45],
]

def main ():
    best_storage_efficiency_value = -1
    best_storage_efficiency_can_name = None
    best_cost_efficiency_value = -1
    best_cost_efficiency_can_name = None
    for row in list:
        name = row[0]
        radius = row[1]
        height = row[2]
        cost = row[3]
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        if storage_efficiency > best_storage_efficiency_value:
            best_storage_efficiency_value = storage_efficiency
            best_storage_efficiency_can_name = name
        if cost_efficiency > best_cost_efficiency_value:
            best_cost_efficiency_value = cost_efficiency
            best_cost_efficiency_can_name = name
        print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')
    print(f'The best storage efficiency can is: {best_storage_efficiency_can_name}')
    print(f'The best cost efficiency can is: {best_cost_efficiency_can_name}')

def compute_volume(radius, height):
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost):
    return compute_volume(radius, height) / cost


main()
