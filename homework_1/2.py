w = float(input("Enter the first number (w): "))
x = float(input("Enter the second number (x): "))
y = float(input("Enter the third number (y): "))
z = float(input("Enter the fourth number (z): "))
sorted_numbers = sorted([w, x, y, z], reverse=True)
for number in sorted_numbers:
    print(number)
