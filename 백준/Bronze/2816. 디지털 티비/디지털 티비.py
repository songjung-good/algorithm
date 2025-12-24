N = int(input())
channel=[input() for _ in range(N)]
now = 0
ans = ''
for i in range(0, N):
    if channel[i] == 'KBS1':
        for j in range(now, 0, -1):
            channel[j], channel[j-1] = channel[j-1], channel[j]
            ans += '4'
            now -= 1
        break
    else:
        now += 1
        ans += '1'
for i in range(0, N):
    if channel[i] == 'KBS2':
        for j in range(now, 1, -1):
            channel[j], channel[j-1] = channel[j-1], channel[j]
            ans += '4'
    else:
        now += 1
        ans += '1'
print(ans)