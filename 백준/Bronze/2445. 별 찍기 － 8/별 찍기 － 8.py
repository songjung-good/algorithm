# 코드를 작성해주세요
N = int(input())
for i in range(1, N+1):
    ans = ''
    ans += '*' * i
    ans += ' ' * (2 * (N-i))
    ans += '*' * i
    print(ans)
for j in range(1, N+1):
    ans = ''
    ans += '*' * (N-j)
    ans += ' ' * (2 * j)
    ans += '*' * (N-j)
    print(ans)
