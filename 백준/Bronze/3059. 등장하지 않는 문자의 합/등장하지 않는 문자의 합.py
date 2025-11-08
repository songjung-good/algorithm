# 코드를 작성해주세요

num = ((65 + 90) * 26) // 2
T = int(input())
for _ in range(T):
    word = set(input())
    now = 0
    for w in word:
        now += ord(w)
    print(num - now)
        