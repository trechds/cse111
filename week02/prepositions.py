import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise, this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise, this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_verbs_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_verbs_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Choose verbs based on quantity and tense.
    if tense == "past":
        verbs = past_verbs
    elif tense == "present" and quantity == 1:
        verbs = present_verbs_singular
    elif tense == "present" and quantity != 1:
        verbs = present_verbs_plural
    elif tense == "future":
        verbs = future_verbs

    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    # Build and return a prepositional phrase.
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

# Exceeding the requirements:
def get_adjective():
    """Return a randomly chosen adjective.
    Return: a randomly chosen adjective.
    """
    adjectives = [
        "beautiful", "happy", "colorful", "mysterious", "energetic", 
        "playful", "curious", "determined", "gentle", "brilliant",
        "vibrant", "graceful", "charming", "radiant", "joyful",
        "majestic", "captivating", "whimsical", "inspiring", "serene"
    ]
    return random.choice(adjectives)

def make_sentence(quantity, tense):
    """Build and return a sentence with four parts:
    a determiner, a noun, a verb, and a prepositional
    phrase. The grammatical quantity of the determiner
    and noun will match the number in the quantity
    parameter. The grammatical quantity and tense of
    the verb will match the number and tense in the
    quantity and tense parameters.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the sentence
            returned from this function should
            be single or pluaral.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a sentence.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    prepositional_phrase = get_prepositional_phrase(quantity)

    # Capitalize the first letter of the sentence and end it with a period.
    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase}."
    return sentence

def main():
    # Print six sentences with different quantities, tenses, and prepositional phrases.
    print("a.", make_sentence(1, "past"))
    print("b.", make_sentence(1, "present"))
    print("c.", make_sentence(1, "future"))
    print("d.", make_sentence(2, "past"))
    print("e.", make_sentence(2, "present"))
    print("f.", make_sentence(2, "future"))

# Call the main function.
main()