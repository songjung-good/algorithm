import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 단어 수 n, 단어 길이 L, 접미사 F
    n, L, F = map(int, input().split())
    lst = list(map(str, input().split()))
    check = {}
    ans = 0
    for i in range(n):
        word = lst[i][L - F:]
        if word in check:
            if check[word]:
                check[word] = False
                ans += 1
            else:
                check[word] = True
        else:
            check[word] = True
    print(ans)