DH = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

def CHECK(day, BOX, T_list):
    DAY = day
    CNT = 0
    while T_list:
        t_list = []
        for T in T_list:
            a, b, c = T
            for d in DH:
                dh, dx, dy= d
                A, B, C = dh+a, dx+b, dy+c
                if 0 <= A < H and 0 <= B < N and 0 <= C < M:
                    if BOX[A][B][C] == 0:
                        BOX[A][B][C] = 1
                        CNT += 1
                        t_list.append((A,B,C))

        if t_list == []:
            DAY -= 1
        DAY += 1
        T_list = t_list

    if CNT != T_CNT:
        DAY = -1
    return DAY

M, N, H = map(int, input().split())
BOX = []
chest = []
T_CNT = 0

for h in range(H):
    BOX_h = []
    for n in range(N):
        tomato = list(map(int, input().split()))
        BOX_h.append(tomato)
        for m in range(M):
            if tomato[m] == 1:
                chest.append((h,n,m))
            if tomato[m] == 0:
                T_CNT += 1
    BOX.append(BOX_h)

print(CHECK(0, BOX, chest))