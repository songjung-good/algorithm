'''
65 대문자
97 소문자
32 차이
'''
word = input()
lst = []
for i in word:
    A = ord(i)
    if A >= 97:
        A -= 32
    lst.append(A)
lst.sort()

max_num = 0
cnt = 0
ans = ''
now_word = chr(lst[0])


for num in lst:
    i = chr(num)
    if i == now_word:
       cnt+=1
    else:
        if max_num == cnt:
            ans = '?'
        elif max_num < cnt:
            max_num = cnt
            ans = now_word
        now_word = i
        cnt = 1
if max_num == cnt:
    ans = '?'
elif max_num < cnt:
    max_num = cnt
    ans = now_word
now_word = i
cnt = 1
print(ans)
