def ten_to_two(num):
    num_new = '0.'

    while num > 0:
        num *= 2
        if num >= 1:
            num_new += '1'
            num -= 1
        else:
            num_new += '0'

    return num_new

num = 0.625
num_new = ten_to_two(num)
print(f"Binary fraction of {num}: {num_new}")