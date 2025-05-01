T = int(input())

for t in range(T):
    input()
    N = int(input())
    total = 0
    for _ in range(N):
        total += int(input())
    
    if total % N:
        print('NO')
    else:
        print('YES')