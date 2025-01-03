# 코드를 작성해주세요
word = input()
N = len(word)
ans = 'true'
for n in range(N//2):
    if word[n] == word[(0-(n+1))]:
        pass
    else:
        ans = 'false'
        break

print(ans)