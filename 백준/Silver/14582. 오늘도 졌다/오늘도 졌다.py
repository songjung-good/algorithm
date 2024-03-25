A = list(map(int, input().split()))
B = list(map(int, input().split()))
team_A = 0
team_B = 0
ans = 'No'
for i in range(18):
  if i % 2 == 0:
    team_A += A[i//2]
  else:
    team_B += B[(i-1)//2]
  if team_A > team_B:
    ans = 'Yes'

print(ans)