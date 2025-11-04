import sys
input = sys.stdin.readline

N = int(input())
D_lst = ['ChongChong']
ans = 1
for _ in range(N):
    A, B = map(str, input().split())
    if A in D_lst and B not in D_lst:
        D_lst.append(B)
        ans += 1
    elif B in D_lst and A not in D_lst:
        D_lst.append(A)
        ans += 1

print(ans)
