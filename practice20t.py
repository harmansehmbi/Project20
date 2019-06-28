import matplotlib.pyplot as plt
import numpy as np

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [11, 13, 21, 34, 45, 56, 67, 78, 82, 91]

X1 = np.random.randn(100)
Y1 = np.random.randn(100)

plt.scatter(X, Y)
plt.scatter(X1, Y1)

plt.show()