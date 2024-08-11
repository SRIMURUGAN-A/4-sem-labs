#Normal curve
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mean = 0
std_dev = 1
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, mean, std_dev)


plt.plot(x, y, label=f'Normal Distribution (mean={mean}, std={std_dev})')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Curve')
plt.legend()
plt.show()


# correlation and scatter plot

np.random.seed(0)
x = np.random.normal(0, 1, 100)
y = 2*x + np.random.normal(0, 1, 100)

plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()
  

  
# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient}")
