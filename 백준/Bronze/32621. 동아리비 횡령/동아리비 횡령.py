# 코드를 작성해주세요
word = list(map(str, input().split('+')))
ans = 'No Money'
if len(word) == 2 and word[0] and word[1] and word[0].isdigit() and word[1].isdigit() and word[0][0] != '0' and word[1][0] != '0' and word[0] == word[1]:
    ans = 'CUTE'

print(ans)  

