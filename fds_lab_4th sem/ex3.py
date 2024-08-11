#frequency dist
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Sample data
data = [23, 21, 23, 24, 22, 24, 23, 25, 26, 25, 27, 24, 23, 22, 24, 23]

def freq_dist (data):
    distribution = Counter(data)
    frequency = pd.DataFrame(list(distribution.items()), columns=['Value', 'Frequency'])
    print(distribution)
    return frequency
freq_dist_df =freq_dist(data)
print(freq_dist_df)
      

# Average
avg = np.average(data)
mean = np.mean(data)
median = np.median(data)
mode = Counter(data).most_common(1)[0][0]
std = np.std(data)
var = np.var(data)
print(avg, mean, median,mode, std, var)



plt.bar(freq_dist_df['Frequency'], freq_dist_df['Value'], color='skyblue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Frequency Distribution')
plt.show()