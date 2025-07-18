N = int(input())
for _ in range(N):
    id, S, I, T = map(int, input().split())
    total = S+I+T
    ans = 'FAIL'
    if total >= 55 and S >= 35*0.3 and I >= 25*0.3 and 40 *0.3:
        ans = 'PASS'

    print(id, total, ans)