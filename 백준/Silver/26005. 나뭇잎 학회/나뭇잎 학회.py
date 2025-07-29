N = int(input())
num = N ** 2
ans = 0
if num == 1:
    ans = 0
elif num % 2:
    ans = num // 2 + 1
else:
    ans = num // 2

print(ans)