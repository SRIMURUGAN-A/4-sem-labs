import numpy as np
from scipy import stats

# Generate synthetic data
np.random.seed(0)
group1 = np.random.normal(10, 2, 100)  # Mean=10, Stddev=2, N=100
group2 = np.random.normal(12, 2, 100)  # Mean=12, Stddev=2, N=100

# Perform the independent t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
