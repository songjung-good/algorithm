# 코드를 작성해주세요
N = input()
cnt = 0
word = N[0]
for n in N:
    if n == word:
        cnt += 1
    else:
        break
print(cnt)