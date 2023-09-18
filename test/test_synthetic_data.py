from collections import defaultdict
from datetime import datetime

from pysynic.synthetic_data import (random_from, randomly_null, random_integer_in_range,
                                    random_date, DATE_FORMAT, random_timestamp)

SAMPLE_SIZE = 10
SAMPLES = list(range(SAMPLE_SIZE))
START_DATE_STR = "1/Jul/2021"
START_DATE = datetime.strptime(START_DATE_STR, DATE_FORMAT)


def test_random_from_list_with_seed():
    num_samples = 20
    results = []
    for i in range(SAMPLE_SIZE * num_samples):
        results.append(random_from(SAMPLES, i))
    assert set(results) == set(SAMPLES)
    assert check_uniform_distribution(results, num_samples) == SAMPLES


def test_random_from_list_based_on_probabilities():
    num_samples = 100
    results = []
    for i in range(SAMPLE_SIZE * num_samples):
        results.append(random_from(SAMPLES))
    check_non_uniform_distribution(results)


def test_randomly_null_with_seed():
    mod = SAMPLE_SIZE // 2
    results = []
    for i, x in enumerate(SAMPLES):
        results.append(randomly_null(x, i, mod))
    assert len([x for x in results if x is None]) == SAMPLE_SIZE / mod


def test_random_in_range_probabilistically_distributed():
    results = []
    low = 7
    high = 17
    for i in range(1000):
        results.append(random_integer_in_range(low, high))
    assert min(results) == low
    assert max(results) == high
    check_non_uniform_distribution(results)


def test_random_date_with_seed():
    results = []
    for i in range(1000):
        results.append(random_date(i, 31, START_DATE_STR))
    assert min(results) == START_DATE
    assert max(results) == datetime.strptime("31/Jul/2021", DATE_FORMAT)


def test_random_timestamp():
    results = []
    for i in range(10000):
        results.append(random_timestamp(None, 31, START_DATE_STR))
    assert min(results) >= START_DATE
    assert max(results) < datetime.strptime("1/Aug/2021", DATE_FORMAT)
    check_non_uniform_distribution(results)


def test_random_timestamp_with_1day_window():
    results = []
    for i in range(10000):
        results.append(random_timestamp(None, 1, START_DATE_STR))
    assert min(results) >= START_DATE
    assert max(results) < datetime.strptime("2/Jul/2021", DATE_FORMAT)


def check_non_uniform_distribution(results: list):
    counts = histogram_of(results)
    assert len(counts) > 1


def histogram_of(results: list) -> dict:
    counts = defaultdict(int)
    for x in results:
        count = counts[x]
        counts[x] = count + 1
    return counts


def check_uniform_distribution(results: list, expected_count: int) -> []:
    counts = histogram_of(results)
    for k, v in counts.items():
        assert v == expected_count
    return list(counts.keys())
    

def count_of(seek, xs: list) -> int:
    return len([x for x in xs if x == seek])
