N = int(input())
BOX = [
    ['@','@','@',' ','@'],
    ['@',' ','@',' ','@'],
    ['@',' ','@',' ','@'],
    ['@',' ','@',' ','@'],
    ['@',' ','@','@','@'],
]

ans = []
for line in BOX:
    now = ''
    for i in range(5):
        now += (line[i] * N)
    for _ in range(N):
        ans.append(now)

for i in ans:
    print(i)