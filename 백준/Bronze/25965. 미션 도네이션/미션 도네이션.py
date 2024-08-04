# 게임 수
N = int(input())
for n in range(N):
    KDA = []
    # 미션 수
    M = int(input())
    for m in range(M):
        kda = list(map(int, input().split()))
        KDA.append(kda)

    ans = 0
    K, D, A = map(int, input().split())
    for k, d, a in KDA:
        plus = (k * K) + (a * A) - (d * D)
        if plus > 0 :
            ans = ans + (k * K) + (a * A) - (d * D)

    print(ans)