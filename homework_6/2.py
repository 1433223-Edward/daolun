import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.random.rand(100)
y3 = np.random.randint(1, 10, 10)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.plot(x, y1, label='Sin Curve')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.subplot(1, 3, 2)
plt.scatter(x, y2, color='red', marker='o', label='Random Points')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.subplot(1, 3, 3)
categories = np.arange(1, 11)
plt.bar(categories, y3, color='green', label='Random Bars')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()

plt.tight_layout()

plt.show()
