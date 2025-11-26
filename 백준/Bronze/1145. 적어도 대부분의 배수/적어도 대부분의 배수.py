import sys, math
input = sys.stdin.readline

lst = list(map(int, input().split()))
ans = float('inf')

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            num = math.lcm(lst[i], lst[j], lst[k])
            if ans > num:
                ans = num

print(ans)