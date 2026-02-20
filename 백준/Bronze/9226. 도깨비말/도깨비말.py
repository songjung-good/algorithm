# 코드를 작성해주세요
while True:
    word = input()
    ans = ''
    if word == '#':
        break
    else:
        temp = ''
        for w in range(len(word)):
            if word[w] in ['a', 'e', 'i', 'o', 'u']:
                ans = word[w:] + temp
                break
            else:
                temp += word[w]
        if ans == '':
            print(word + 'ay')
        else:
            print(ans + 'ay')