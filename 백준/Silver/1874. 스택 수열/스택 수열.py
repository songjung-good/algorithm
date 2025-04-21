import sys
input = sys.stdin.readline
S = []
N = int(input())
now = 0
ans = []
check = True

for _ in range(N):
    n = int(input())
    while True:
        if n > now:
            S.append(now+1)
            now += 1
            ans.append('+')
        else:
            x = S.pop()
            if x == n:
                ans.append('-')
            else:
                check = False
            break
    if not check:
        print('NO')
        exit()

for i in ans:
    print(i)