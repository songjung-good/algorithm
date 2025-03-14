N = int(input())
N_lst = []
Q = [0] * N
for _ in range(N):
    x, y = map(int,input().split())
    N_lst.append((x,y))

x, y = N_lst[N-1]
if x == 1:
    Q[N-1] = y

for n in range(N-1,-1,-1):
    day, inc = N_lst[n]
    if n + day > N:
        inc = 0
    elif n + day == N:
        pass
    else:
        inc += Q[n+day]
    Q[n] = max(max(Q[n:]), inc)

print(Q[0])
