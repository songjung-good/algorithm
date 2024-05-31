A = int(input())
나머지 = A % 5
if 나머지 > 0:
    print(A//5 + 1)
else:
    print(A//5)