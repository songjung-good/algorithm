# 코드를 작성해주세요
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    score = [[0, 0] for _ in range(n+1)]
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        score[a][0] += p
        score[a][1] += q
        score[b][0] += q
        score[b][1] += p
    
    ans = []
    for i in range(1, n+1):
        S, A = score[i]
        if S == 0:
            W = 0
        else:
            W = S**2 / (S**2 + A**2)
        ans.append(W * 1000)
    
    print(int(max(ans)))
    print(int(min(ans)))
