def is_prime(a):
    if a <= 1:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3, int(a**0.5) + 1, 2):
            if a % i == 0:
                return False
        return True

number_to_check = int(input("Enter a number: "))

if is_prime(number_to_check):
    print("YES.")
else:
    print("NO.")
