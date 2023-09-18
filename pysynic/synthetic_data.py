from typing import Optional
import random as random
from datetime import datetime, timedelta

DATE_FORMAT = '%d/%b/%Y'
SECONDS_IN_DAY = 24 * 3600


def random_from(xs: list, seed: int = None) -> Optional[str]:
    """
    Returns random value from list
    :param xs: list of values
    :param seed: Ensures some determinism if not None.
    :return: Value from list chosen at (semi)random
    """
    if len(xs) == 0:
        return None
    index = random.randint(1, len(xs)) - 1
    if seed is not None:
        index = seed % len(xs)
    return xs[index]


def randomly_null(x, seed: int = None, every=2):
    """
    (Semi)randomly turns a value into None
    :param x: The value that will (potentially) become None
    :param seed: An optional value that makes the output deterministic
    :param every: The value returned will be None every mod times, either on average or strictly
    deterministically depending on the value of seed
    :return: either x or None
    """
    if seed is not None:
        if seed % every == 1:
            return None
        else:
            return x
    else:
        if random.randint(1, every) == 1:
            return None
        else:
            return x


def random_integer_in_range(lower_inc: int, upper_inc: int, seed: int = None) -> int:
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


def random_date(seed: int, max_delta: int, start_date: str) -> datetime:
    """
    Returns a random date within an open range.
    :param seed: Adds determinism if not None
    :param max_delta: The total size of the date window in units of days
    :param start_date: The earliest date that can be returned. For example: '1/Jul/2021'
    :return: a (potentially) random date within the window
    """
    if seed is None:
        n_days = random.randint(0, max_delta)
    else:
        n_days = seed % max_delta
    return datetime.strptime(start_date, DATE_FORMAT) + timedelta(days=n_days)


def random_timestamp(seed: Optional[int], max_delta: int, start_date: str) -> datetime:
    """
    Returns a random timestamp within a window.
    Be careful of daylight saving with this method as DST can cause unexpected results...
    :param seed: Adds determinism if not None
    :param max_delta: The size of the date window in units of days
    :param start_date: The earliest date that can be returned. For example: '1/Jul/2021'
    :return: a (potentially) random timestamp within the window
    """
    if seed is not None:
        time = timedelta(seconds=seed % SECONDS_IN_DAY)
    else:
        time = timedelta(seconds=random.randint(0, SECONDS_IN_DAY - 1))
    return random_date(seed, max_delta - 1, start_date) + time
