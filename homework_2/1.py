n=int(input("Please enter the number:"))
if n == 1:
    print("1")
if n == 2:
    print("1*2")
if n == 3:
    print("1*3")
if n == 4:
    print("2*2")
res = 1
while n > 4:
    res *= 3
    n -= 3
    print("3*",end="")
res *= n
print(n)
#当n小于等于4时，其最大值等于n本身，当n大于4时，可以分成多个小于4的数相乘，5=2*3，6=3*3，7=4*3，8=5*3<2*3*3.则发现任何大于4的数都可以化为与3相乘更大的数