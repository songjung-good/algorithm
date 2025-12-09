N = int(input())
for _ in range(N):
    A, B = input().split('-')
    f = 0
    for i in range(3):
        f += (ord(A[i]) - 65) * 26**(2-i)
    
    num = abs(f - int(B))
    if num <= 100:
        print('nice')
    else:
        print('not nice')
    