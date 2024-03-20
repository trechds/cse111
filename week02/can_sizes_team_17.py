#----------------------------------------------------
# Author: Cliff Cummings
# Course: CSE 111
# File: can_sizes.py
#
# In many countries, food is stored in steel cans (also known as tin cans) that are shaped like
# cylinders. There are many different sizes of steel cans. The storage efficiency of a can tells us
# how much a can stores versus how much steel is required to make the can. Some sizes of cans
# require a lot of steel to store a small amount of food. Other sizes of cans require less steel and
# store more food. A can size with a large storage efficiency is considered more friendly to the
# environment than a can size with a small storage efficiency.
#
# The storage efficiency of a steel can is computed by dividing the volume of a can by its surface
# area.
#
# storage_efficiency = volume / surface_area
# In other words, the storage efficiency of a can is the space inside the can divided by the amount
# of steel required to make the can. The formulas for the volume and surface area of a cylinder are:
# 
# volume = π radius**2 height
# surface_area = 2π radius (radius + height)
#
#----------------------------------------------------
import math

def main():
    # Declare ordered lists: one string list and three float lists

    can_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    can_radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    can_heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    can_costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    # Compute the following:
    can_volumes = []
    can_surface_areas = []
    storage_effciencies = []

    # print ('\nComputing:')
    for i in range(len(can_names)):
        can = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]
        volume = compute_volume(radius, height)
        can_volumes.append(volume)
        surface_area = compute_surface_area(radius, height)
        can_surface_areas.append(surface_area)
        storage_effciency = compute_storage_efficiency(volume, surface_area)
        storage_effciencies.append(storage_effciency)

        # print(f"{i}: Name = {can}  Radius = {radius:.2f}  Height = {height:.2f}  Volume = {volume:.2f}")
        print(f"{can} {storage_effciency:.2f}")

    print()
    
# volume = π radius**2 height
def compute_volume (radius, height):
    volume = math.pi * radius**2 * height
    return volume

# surface_area = 2π radius (radius + height)     
def compute_surface_area (radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# storage_efficiency = volume / surface_area
def compute_storage_efficiency(volume, surface_area):
    storage_effciency = volume / surface_area
    return storage_effciency

main()