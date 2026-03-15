# 코드를 작성해주세요
N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for k in range((K+1)//2):
    ans += lst[-1-k]

for k in range((K-1)//2):
    ans -= lst[k]

print(ans)