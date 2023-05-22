"""random_number module uses randint function from random module
and generates random number between provided boundaries.
"""

from random import randint


def generate_random_number(num1: int, num2: int):

    """returns random number based on lowest and highest boundaries."""
    random_number = randint(num1, num2) if num1 < num2 else randint(num2, num1)
    return random_number
