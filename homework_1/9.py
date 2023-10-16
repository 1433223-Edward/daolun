def cubicroot(n, min=1e-10, max=1000):
    x0 = n / 3.0
    for i in range(max):
        x1 = (2 * x0 + n / (x0 * x0)) / 3.0
        if abs(x1 - x0) < min:
            return x1
        x0 = x1
    return x1

n = float(input("Enter a number: "))

result = cubicroot(n)

print(result)
   