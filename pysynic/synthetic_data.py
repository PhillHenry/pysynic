from typing import Optional
import random as random


def random_from(xs: list, seed: int = None) -> Optional[str]:
    """
    Returns random value from list

    Args:
        xs (list): list of values
        seed (int, optional): random number. Defaults to None.

    Returns:
        Optional[str]: Value from list chosen at random
    """
    if len(xs) == 0:
        return None
    index = random.randint(1, len(xs)) - 1
    if seed is not None:
        index = seed % len(xs)
    return xs[index]


def randomly_null(x, seed: int = None, mod=2):
    """

    :param x: The value that will (potentially) become None
    :param seed: An optional value that makes the output deterministic
    :param mod: The value returned will be None every mod times, either on average or strictly
    deterministically depending on the value of seed
    :return: either x or None
    """
    if seed is not None:
        if seed % mod == 1:
            return None
        else:
            return x
    else:
        if random.randint(1, mod) == 1:
            return None
        else:
            return x
