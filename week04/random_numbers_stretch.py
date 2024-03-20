import random

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "horse", "iguana", "jellyfish"]
    for _ in range(quantity):
        random_word = random.choice(word_list)
        words_list.append(random_word)

def main():
    # Create a list of numbers
    numbers = [16.2, 75.1, 52.3]

    # Print the initial list of numbers
    print("Initial List of Numbers:", numbers)

    # Call append_random_numbers with one argument
    append_random_numbers(numbers)

    # Print the list of numbers after adding one random number
    print("List of Numbers After Adding One Random Number:", numbers)

    # Call append_random_numbers with two arguments
    append_random_numbers(numbers, 3)

    # Print the list of numbers after adding three random numbers
    print("List of Numbers After Adding Three Random Numbers:", numbers)

    # Add a list of words
    words = ["python", "programming", "challenge", "team", "stretch", "random"]

    # Call append_random_words with two arguments
    append_random_words(words, 2)

    # Print the list of words after adding two random words
    print("List of Words After Adding Two Random Words:", words)

if __name__ == "__main__":
    main()
