# 코드를 작성해주세요
T = int(input())
for t in range(T):
    lst = list(map(str, input().split()))
    new_word = ''
    for word in lst:
        for w in reversed(word):
            new_word += w
        new_word += ' '
            
    print(new_word[:-1])