import sys
input = sys.stdin.readline

N = int(input())
A_lst = sorted(list(map(int,input().split())), reverse=True)
B_lst = sorted(list(map(int,input().split())))

ans = 0
for n in range(N):
    ans += A_lst[n] * B_lst[n]
print(ans)
