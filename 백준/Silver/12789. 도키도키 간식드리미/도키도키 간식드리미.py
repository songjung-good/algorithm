import sys
input = sys.stdin.readline

N = int(input())
STACK1 = list(map(int, input().split()))
STACK2 = []
STACK1.reverse()

ans = 'Nice'
for n in range(1, N+1):
    check = False
    if n in STACK1:
        while STACK1:
            now = STACK1.pop()
            if now == n:
                check = True
                break
            else:
                STACK2.append(now)
    elif n in STACK2:
        check = False
        while STACK2:
            now = STACK2.pop()
            if now == n:
                check = True
                break
            else:
                break
    if not check:
        ans = 'Sad'
        break

print(ans)
