# 코드를 작성해주세요
for _ in range(int(input())):
    ans = ''
    past = ''
    for w in input():
        if w == past:
            pass
        else:
            ans += w
            past = w
    print(ans)