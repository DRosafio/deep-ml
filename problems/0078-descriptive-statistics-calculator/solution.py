import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    mean = float(np.mean(data))
    med = float(np.median(data))
    def mode(data):
        count = {}
        for x in data:
            count[x] = count.get(x, 0) + 1
        if max(count.values()) == 1:
            return data[0]
        return max(count, key=count.get)
    var = float(np.var(data))
    std = float(np.std(data))
    per_25, per_50, per_75 = float(np.percentile(data, 25)),float(np.percentile(data, 50)),float(np.percentile(data, 75))
    inter = float(per_75-per_25)
    return {'mean': mean, 'median':med, 'mode': mode(data), 'variance': var, 'standard_deviation': std, '25th_percentile': per_25, '50th_percentile': per_50, '75th_percentile': per_75, 'interquartile_range': inter}
