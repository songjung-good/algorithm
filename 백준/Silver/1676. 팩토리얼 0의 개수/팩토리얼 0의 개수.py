A = int(input())

num = 1
for i in range(A - 1):
    num *= (i + 2)

ans = 0
word = str(num)
B = len(word)
for j in range(B):
    if word[-j-1] != '0':
        break
    else:
        ans += 1
print(ans)
