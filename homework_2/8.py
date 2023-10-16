# -*- coding: gbk -*-
import time
import random

# method 1: monte_carlo
def monte_carlo_pi(num):
    inside_circle = 0
    for _ in range(num):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num) * 4

# method 2: Leibniz
def leibniz_pi(num):
    pi_estimate = 0
    for k in range(num):
        pi_estimate += (-1)**k / (2*k + 1)
    return pi_estimate * 4

# method 3: Leibniz variant
def leibniz_variant_pi(num):
    pi_estimate = 0
    sign = 1
    for k in range(num):
        term = sign / (2*k + 1)
        pi_estimate += term
        sign = -sign
    return pi_estimate * 4

# time
num_samples_monte_carlo = 1000000
num_terms_leibniz = 100000

start_time = time.time()
pi_monte_carlo = monte_carlo_pi(num_samples_monte_carlo)
end_time = time.time()
print(f"Monte Carlo π estimation: {pi_monte_carlo}")
print(f"Time taken for Monte Carlo method: {end_time - start_time:.5f} seconds\n")

start_time = time.time()
pi_leibniz = leibniz_pi(num_terms_leibniz)
end_time = time.time()
print(f"Leibniz π estimation: {pi_leibniz}")
print(f"Time taken for Leibniz method: {end_time - start_time:.5f} seconds\n")

start_time = time.time()
pi_leibniz_variant = leibniz_variant_pi(num_terms_leibniz)
end_time = time.time()
print(f"Leibniz variant π estimation: {pi_leibniz_variant}")
print(f"Time taken for Leibniz variant method: {end_time - start_time:.5f} seconds")
