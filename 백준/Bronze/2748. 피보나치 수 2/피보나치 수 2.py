N=int(input())
a,b=0,1
if N == 0:
    pass
else:
    for _ in range(N):
        a, b = b, a+b
print(a)