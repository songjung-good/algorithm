T = int(input())

for tc in range(T):
    res = input()
    plus = 1
    ans = 0
    for i in res:
        if i == 'X':
            plus = 1
        else:
            ans += plus
            plus += 1

    print(ans)
