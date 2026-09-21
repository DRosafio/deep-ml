def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    res = []
    samp = set(samples)
    for n in samp:
        res.append((n, samples.count(n)/len(samples)))
    return res