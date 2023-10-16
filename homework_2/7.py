def cube_root(c, initial=1.0, limit=1e-6, max=1000):
    g = initial
    iterations = 0

    while abs(g**3 - c) >= limit and iterations < max:
        g = (2 * g + c / (g**2)) / 3
        iterations += 1

    return g, iterations

c = 27 
initial = 1.0 
result, iterations = cube_root(c, initial)

print(f"Approximate cube root of {c}: {result}")
print("Number of iterations:", iterations)
