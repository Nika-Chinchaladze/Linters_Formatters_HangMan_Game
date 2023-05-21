"""random_number module uses randint function from random module and generates random number between
provided boundaries.
"""

from random import randint


def generate_random_number(first: int, second: int):
    """returns random number based on lowest and highest boundaries."""
    random_number = randint(first, second) if first < second else randint(second, first)
    return random_number
