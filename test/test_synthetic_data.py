from pysynic.synthetic_data import random_from

sample_size = 10
samples = list(range(sample_size))


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
