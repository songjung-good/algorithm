# 케이스 수 T, 사탕 수 J, 상자 수 N
T = int(input())
for t in range(T):
    J, N = map(int, input().split())

    # 세로길이 R, 가로길이 C
    BOX = []
    for n in range(N):
        R, C = map(int, input().split())
        BOX.append(R*C)
    BOX.sort(reverse=True)

    # 사용하는 상자의 개수
    ans = 0
    while J > 0:
        for box in BOX:
            J = J - box
            ans = ans + 1
            if J > 0:
                pass
            else:
                break
    print(ans)