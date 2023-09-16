from pysynic.synthetic_data import random_from
import numpy as np


def test_random_from_list_with_seed():
    n = 10
    xs = list(range(n))
    m = 20
    results = []
    for i in range(n * m):
        results.append(random_from(xs, i))
    assert set(results) == set(xs)
    check_uniform_distribution(results, xs, m)


def check_uniform_distribution(results: list, xs: list, expected_count: int):
    for i in xs:
        assert count_of(i, results) == expected_count
    

def count_of(seek, xs) -> int:
    return len([x for x in xs if x == seek])
