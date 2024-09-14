N = int(input())
A, B, C = map(int, input().split())
ans = 0
if A > N:
    ans = ans + N
else:
    ans = ans + A
if B > N:
    ans = ans + N
else:
    ans = ans + B
if C > N:
    ans = ans + N
else:
    ans = ans + C

print(ans)

