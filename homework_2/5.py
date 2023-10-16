def sqrt_2(initial):
    g = initial
    limit = 1e-6

    while abs(g * g - 2) >= limit:
        g = 0.5 * (g + 2 / g)

    return g

result_with_c_2 = sqrt_2(2)
result_with_c_2000 = sqrt_2(2000)

print(result_with_c_2)
print(result_with_c_2000)
