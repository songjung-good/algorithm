A, B = map(int, input().split())
R = [A]
C = [B]
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0:
        C.append(y)
    else:
        R.append(y)

R.sort()
C.sort()
past_R = 0
ans = 0
for r in R:
    now_r = r - past_R
    past_C = 0
    for c in C:
        now_c = c - past_C
        cnt = now_c * now_r
        if cnt > ans:
            ans = cnt
        past_C = c
    past_R = r

print(ans)