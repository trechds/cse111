import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            student_dict[row[0]] = row[1]
    return student_dict

def remove_dashes(inumber):
    """Remove dashes from the input I-Number."""
    return inumber.replace('-', '')

def validate_inumber(inumber):
    """Validate the input I-Number."""
    inumber = remove_dashes(inumber)
    if not inumber.isdigit():
        return False, "Invalid I-Number"
    if len(inumber) < 9:
        return False, "Invalid I-Number: too few digits"
    if len(inumber) > 9:
        return False, "Invalid I-Number: too many digits"
    return True, inumber

def main():
    # Read the dictionary from the CSV file
    filename = 'students.csv'
    student_dict = read_dictionary(filename)

    # Get an I-Number from the user
    inumber = input("Enter the I-Number: ")

    # Validate the I-Number
    is_valid, inumber = validate_inumber(inumber)
    if not is_valid:
        print(inumber)
        return

    # Remove dashes from the I-Number
    inumber = remove_dashes(inumber)

    # Look up the student name in the dictionary
    student_name = student_dict.get(inumber, "No such student")

    # Print the student name
    print("Student name:", student_name)

if __name__ == "__main__":
    main()
