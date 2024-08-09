# 교과서
word = input()
# 찾는 단어
keyword = input()
# 숫자 제거
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 교과서에서 숫자 제거
new_word = ''
for k in word:
    if k in number:
        pass
    else:
        new_word = new_word + k

if keyword in new_word:
    print(1)
else:
    print(0)
'''
# 찾는 단어의 길이 A, 새 단어의 길이 B, 찾는 단어의 첫 글자 first
A = len(keyword)
B = len(new_word)
first = keyword[0]
ans = 0
# 예외
if new_word == keyword:
    print(1)
elif A > B:
    print(ans)
# 새 단어에서 글자 찾기
else:
    for j in range(B):
        # 첫글자 맞춰보고 같으면 거기서부터 맞추기
        if first == new_word[j]:
            now = 1
            for l in range(j+1, B):
                if now == A-1:
                    ans = 1
                    break
                if new_word[l] == keyword[now]:
                    now += 1
                    pass
                else:
                    break
        else:
            pass

    print(ans)'''