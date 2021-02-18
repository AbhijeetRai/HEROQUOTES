from random import randint
from quotes import quotes_dict

"""
    Quotes are stored in the Dictionary quotes_dict in quotes.py
"""


def quote():
    """
        A quote from marvel movie or comics
        or a quote from dc movie or comics will be printed
        """

    return quotes_dict[randint(0, 74)]
