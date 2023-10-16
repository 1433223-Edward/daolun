def generate_array_b(a):
    n = len(a)
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i - 1] * a[i]
    return b

a = [1, 2, 3, 4, 5]

b = generate_array_b(a)
print("Array a:", a)
print("Array b:", b)
