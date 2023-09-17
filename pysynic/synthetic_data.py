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
    (Semi)randomly turns a value into None
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


def random_in_range(lower_inc: int, upper_inc: int, seed: int = None) -> int:
    """
    Returns a (semi) random int within a range.
    :param lower_inc: The lowest possible value
    :param upper_inc: The highest possible value
    :param seed: Adds determinism if not null, otherwise the returned value is follows a uniform
    distribution
    :return: A random int in the range [lower_inc, upper_inc]
    """
    if seed is not None:
        delta = upper_inc - lower_inc
        return lower_inc + (seed % delta)
    else:
        return random.randint(lower_inc, upper_inc)

