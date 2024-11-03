# 코드를 작성해주세요
N, M = map(int, input().split())
ans = []
num = []
for n in range(N):
    streak = list(map(str, input().split()))
    max = 0
    now = 0
    for m in range(M):
        word = streak[m]
        if word == '*':
            if max < now:
                max = now
            now = 0
        else:
            now += 1
        if m == M-1:
            if max < now:
                max = now
                now = 0
    ans.append(f'{max} {streak[-1]}')
    if max in num:
        pass
    else:
        num.append(max)
print(len(num))
for a in range(N):
    print(ans[a])