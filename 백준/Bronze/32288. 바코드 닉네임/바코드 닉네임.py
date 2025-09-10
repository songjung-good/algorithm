N = int(input())
word = input()
ans = ''
for w in word:
    if w == 'I':
        ans += 'i'
    else:
        ans += 'L'
print(ans)