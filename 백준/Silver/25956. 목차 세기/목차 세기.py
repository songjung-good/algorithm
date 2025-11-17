import sys
input = sys.stdin.readline

N = int(input())

level_last = [0] * (N + 1)     # 각 레벨의 마지막 노드 index
cnt_lst = [0] * N              # 정답(각 노드의 자식 수)
levels = [0] * N               # 각 노드의 레벨 저장

for n in range(N):
    now = int(input())
    if n == 0:
        if now != 1:
            print(-1)
            exit()
        levels[n] = now
        level_last[now] = 0

    else:
        prev = levels[n - 1]

        if now > prev + 1:
            print(-1)
            exit()

        else:
            levels[n] = now
            if now == 1:
                level_last[now] = n

            else:
                parent_idx = level_last[now-1]
                cnt_lst[parent_idx] += 1

                level_last[now] = n

for i in range(N):
    print(cnt_lst[i], end='\n')