word = input()
check = ['a', 'e', 'i', 'o', 'u']
while word != '#':
    ans = 0
    for i in word:
        i = i.lower()
        if i in check:
            ans += 1
    print(ans)
    word = input()