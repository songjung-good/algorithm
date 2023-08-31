N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
ans = 0
for i in score:
    new_score = i / max_score * 100
    ans += new_score
print(ans/N)