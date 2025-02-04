from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    Q = deque((imp, idx) for idx, imp in enumerate(N_lst))
    cnt = 0

    while Q:
        current_imp, current_idx = Q.popleft()
        is_highest = True

        for imp, _ in Q:
            if imp > current_imp:
                is_highest = False
                break

        if is_highest:
            cnt += 1
            if current_idx == M:
                print(cnt)
                break
        else:
            Q.append((current_imp, current_idx))