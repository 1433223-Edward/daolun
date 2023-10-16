def sqrt_2(initial):
    g = initial
    limit = 1e-6

    while abs(g * g - 2) >= limit:
        g = 0.5 * (g + 2 / g)

    return g

c = 2

result_with_c_over_2 = sqrt_2(c / 2)
result_with_c = sqrt_2(c)
result_with_c_over_4 = sqrt_2(c / 4)

print(result_with_c_over_2)
print(result_with_c)
print(result_with_c_over_4)