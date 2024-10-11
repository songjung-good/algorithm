A = int(input())

cnt = 1
ans = 1

for a in range(2, A):
    cnt += a
    ans += 1
    if cnt >= A:
        break

if cnt > A:
    ans -= 1

print(ans)