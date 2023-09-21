N = int(input())
ans = 0
for i in range(N):
    word = input()
    word_lst = []
    cnt = True
    past_word = ''
    for i in word:
        if i != past_word:
            if i in word_lst:
                cnt = False
                break
            else:
                word_lst.append(i)
        past_word = i
    if cnt:
        ans += 1
print(ans)