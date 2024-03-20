# The standard Python random module includes a function named choice that
# randomly chooses one element from a list and returns that element.
# The choice function is easy to call like this:

import random

# Create a list of strings and assign
# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
word = random.choice(words)


# The Python str.capitalize method will capitalize the first letter in a word. The capitalize method is easy to call like this:


# This could be any word from any source.
word = "horse"

# Call the capitalize method which will
# capitalize the first letter of the word.
cap_word = word.capitalize()



# In Python, it is easy to use an f-string to combine many strings into one large string like this:


given = "Michelle"
middle = "Aya"
surname = "Takechi"

full_name = f"{given} {middle} {surname}"