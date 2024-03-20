import random
import math

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    print()
    append_random_numbers(numbers)
    print(numbers)
    print()
    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(numbers_list, quantity = 1):
    for i in range(quantity):
        number = random.uniform(1, 100)
        rounded = round(number, 1)
        numbers_list.append(rounded)

if __name__ == "__main__":
    main()