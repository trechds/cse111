# Open the provinces.txt file for reading
with open('provinces.txt', 'r') as file:
    # Read the contents of the file into a list
    provinces_list = file.readlines()

# Strip newline characters from each element in the list
provinces_list = [province.strip() for province in provinces_list]

# Print the entire list
print("Original list of provinces:")
print(provinces_list)

# Remove the first element from the list
first_province = provinces_list.pop(0)
print("\nRemoved the first province:", first_province)

# Remove the last element from the list
last_province = provinces_list.pop()
print("Removed the last province:", last_province)

# Replace all occurrences of "AB" in the list with "Alberta"
provinces_list = [province.replace('AB', 'Alberta') for province in provinces_list]

# Count the number of elements that are "Alberta" and print that number
count_alberta = provinces_list.count('Alberta')
print("\nNumber of provinces named Alberta:", count_alberta)

# Print the modified list
print("\nModified list of provinces:")
print(provinces_list)
