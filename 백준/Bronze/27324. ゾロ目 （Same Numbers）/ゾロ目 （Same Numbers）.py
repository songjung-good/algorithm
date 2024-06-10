A = int(input())

a = A % 10
b = A - (a*10)

if a == b:
    print(1)
else:
    print(0)