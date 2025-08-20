# 코드를 작성해주세요
while True:
    word = input()
    cnt = 0
    if word[0] == '#':
        break
    else:
        w = word[0]
        for i in word[1:]:
            if w == i:  
                cnt += 1
            elif w == i.lower():
                cnt += 1
    print(w, cnt)
    