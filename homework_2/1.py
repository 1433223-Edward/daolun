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
#��nС�ڵ���4ʱ�������ֵ����n������n����4ʱ�����Էֳɶ��С��4������ˣ�5=2*3��6=3*3��7=4*3��8=5*3<2*3*3.�����κδ���4���������Ի�Ϊ��3��˸������