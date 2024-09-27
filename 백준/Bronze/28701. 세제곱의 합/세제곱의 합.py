N = int(input())
num1 = 0
for n1 in range(1, N+1):
    num1 = num1 + n1

num2 = num1 ** 2

num3 = 0
for n2 in range(1, N+1):
    num3 = num3 + (n2**3)

print(num1)
print(num2)
print(num3)