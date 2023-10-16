import random
import math 

def f(x):
    return x**2 + 4 * x * math.sin(x)

def monte_carlo_integration(num_samples, a, b):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += f(x)

    average = total / num_samples
    return average * (b - a)


a = 2
b = 3

num_samples = 100000

estimated_integral = monte_carlo_integration(num_samples, a, b)
print(estimated_integral)
