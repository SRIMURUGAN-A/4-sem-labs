import numpy as np
import pandas as pd
from scipy import stats
# Generate synthetic data for three groups
np.random.seed(0)
group1 = np.random.normal(10, 2, 30)
group2 = np.random.normal(12, 2, 30)
group3 = np.random.normal(11, 2, 30)
# Perform the one-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-statistic: {f_stat}")
print(f"P-value: {p_value}")
