N = int(input())
X, S = map(int, input().split())
ans = 'NO'

for _ in range(N):
    A, B = map(int, input().split())
    if ans == 'YES':
        break
    elif A <= X and S < B:
        ans = 'YES'
    else:
        pass

print(ans)
