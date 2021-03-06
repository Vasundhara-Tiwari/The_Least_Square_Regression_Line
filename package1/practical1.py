import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 2, 6, 8, 10])
y = np.array([0, 1, 2, 3, 3])

sum_x = sum(x)
sum_y = sum(y)

x_square = x*x
xy = x*y

sum_xy = sum(xy)
sum_x_square = sum(x_square)

SSxx = sum_x_square - (1 / len(x) * sum_x * sum_x)
SSxy = sum_xy - (1 / len(x) * sum_x * sum_y)

x_bar = sum_x / len(x)
y_bar = sum_y / len(y)

beta1 = SSxy / SSxx
beta0 = y_bar - beta1 * x

y_cap = beta1 * x - beta0

print(y_cap)
print(x)

plt.plot(x, y_cap)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
