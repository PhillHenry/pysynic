from pysynic.synthetic_data import (random_from, randomly_null, random_integer_in_range,
                                    random_date, DATE_FORMAT, random_timestamp)
from datetime import datetime, timedelta

sample_size = 10
samples = list(range(sample_size))
START_DATE_STR = "1/Jul/2021"
START_DATE = datetime.strptime(START_DATE_STR, DATE_FORMAT)


def test_random_from_list_with_seed():
    num_samples = 20
    results = []
    for i in range(sample_size * num_samples):
        results.append(random_from(samples, i))
    assert set(results) == set(samples)
    counts = check_uniform_distribution(results, samples, num_samples)
    assert len(set(counts)) == 1


def test_random_from_list_based_on_probabilities():
    num_samples = 100
    results = []
    for i in range(sample_size * num_samples):
        results.append(random_from(samples))
    check_non_uniform_distribution(results)


def test_randomly_null_with_seed():
    mod = sample_size // 2
    results = []
    for i, x in enumerate(samples):
        results.append(randomly_null(x, i, mod))
    assert len([x for x in results if x is None]) == sample_size / mod


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


def test_random_timestamp_with_1day_window():
    results = []
    for i in range(10000):
        results.append(random_timestamp(None, 1, START_DATE_STR))
    assert min(results) >= START_DATE
    assert max(results) < datetime.strptime("2/Jul/2021", DATE_FORMAT)


def check_non_uniform_distribution(results: list):
    counts = set()
    for x in samples:
        counts.add(count_of(x, results))
    assert len(counts) > 1


def check_uniform_distribution(results: list, xs: list, expected_count: int) -> [int]:
    counts = []
    for i in xs:
        count = count_of(i, results)
        assert count == expected_count
        counts.append(count)
    return counts
    

def count_of(seek, xs: list) -> int:
    return len([x for x in xs if x == seek])
