N = int(input())
ans1 = 0
ans2 = 0
for i in range(0, N-2):
    ans2 += i+1
    ans1 += ans2
print(ans1)
print(3)