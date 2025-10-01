n = int(input())
A, B = 100, 100
for _ in range(n):
    x, y = map(int,input().split())
    if x > y: B -= x 
    elif x < y: A -= y
print(A)
print(B)