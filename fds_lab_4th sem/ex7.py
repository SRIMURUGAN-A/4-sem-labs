import numpy as np
from scipy import stats

# Generate synthetic data for two groups
np.random.seed(0)
group1 = np.random.normal(10, 2, 100)  # Mean=10, Stddev=2, N=100
group2 = np.random.normal(12, 2, 100)  # Mean=12, Stddev=2, N=100

# Calculate means and standard deviations
mean1 = np.mean(group1)
mean2 = np.mean(group2)
std1 = np.std(group1, ddof=1)
std2 = np.std(group2, ddof=1)
n1, n2 = len(group1), len(group2)

# Calculate the standard error of the difference
se = np.sqrt(std1**2/n1 + std2**2/n2)

# Calculate the z-score
z = (mean1 - mean2) / se

# Calculate the p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"Z-score: {z}")
print(f"P-value: {p_value}")
