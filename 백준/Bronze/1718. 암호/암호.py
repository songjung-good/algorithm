# 코드를 작성해주세요
word = input()
word_lst = []
for w in word:
    word_lst.append(ord(w))

pw = input()
pw_lst = []
for p in pw:
    pw_lst.append(ord(p))

ans = ''
wd_cnt = len(word_lst)
pw_cnt = len(pw_lst)
for c in range(wd_cnt):
    now_word = word_lst[c]
    if now_word == 32:
        ans += ' '
    else:
        cnt = c % pw_cnt
        now_pw = pw_lst[cnt]
        now_word = now_word - now_pw + 96
        if now_word < 97:
            now_word += 26
        ans += chr(now_word)

print(ans)