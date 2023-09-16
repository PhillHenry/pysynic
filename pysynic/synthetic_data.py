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

