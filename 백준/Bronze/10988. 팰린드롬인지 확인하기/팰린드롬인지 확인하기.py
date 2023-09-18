word = input()
N = len(word)
if N == 1:
    ans = 1
else:
    for i in range(N//2):
        if word[i] == word[-i-1]:
            ans = 1
        else:
            ans = 0
            break

print(ans)