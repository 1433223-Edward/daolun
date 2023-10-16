def sqrt_2():
    g = 1.0
    limit = 1e-6

    while abs(g * g - 2) >= limit:
        g = 0.5 * (g + 2 / g)

    return g

result = sqrt_2()
print(result)
