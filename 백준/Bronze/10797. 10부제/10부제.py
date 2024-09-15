N = int(input())
num_list = list(map(int, input().split()))
ans = 0
for i in num_list:
    if i == N:
       ans += 1
print(ans)