# 입력 개수
N = int(input())
# 단어
L = input().upper()
num = 0
ans = 0
for i in L:
    ans += (ord(i) - ord('A') + 1) * (31**num)
    num += 1

print(ans)