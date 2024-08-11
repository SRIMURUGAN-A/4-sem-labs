# Basic matplotlib
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y =[6,7,8,9,10]
plt.plot(x,y)
plt.legend("L")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

import numpy as np
data = np.random.normal(0,10,100)
plt.hist(data, bins=10, color='red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


datas =np.random.normal(0,10,100)
plt.scatter(data,datas)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
