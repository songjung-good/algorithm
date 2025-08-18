N, S, R = map(int, input().split())
S_lst = list(map(int, input().split()))
S_visit = [0] * (N+2)
R_lst = list(map(int, input().split()))
R_visit = [0] * (N+2)

for s in range(S):
    S_visit[S_lst[s]] = 1
for r in range(R):
    R_visit[R_lst[r]] = 1

for i in range(1, N+1):
    if R_visit[i] == 1:
        if S_visit[i] == 1:
            S_visit[i] = 0
            R_visit[i] = 0
        elif S_visit[i-1] == 1:
            S_visit[i-1] = 0
            R_visit[i] = 0
        elif R_visit[i+1] == 0 and S_visit[i+1] == 1:
            S_visit[i+1] = 0
            R_visit[i] = 0


print(sum(S_visit))