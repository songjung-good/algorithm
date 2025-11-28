import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 각 값의 현재 위치 (0-based index)
pos = [0] * (N + 1)
for i, v in enumerate(arr):
    pos[v] = i

cnt_lst = [0] * N  # 각 값(1..N)의 이동 거리

for i in range(N):
    num = i + 1          # 지금 i번째에 와야 할 값
    j = pos[num]         # num이 현재 있는 위치

    if i == j:
        continue         # 이미 제자리에 있으면 스킵

    A = arr[i]           # i 위치 값
    B = arr[j]           # j 위치 값 (== num)
    diff = j - i         # 이동 거리

    # 이동 거리 누적 (값 기준, 그래서 A-1, B-1)
    cnt_lst[A - 1] += diff
    cnt_lst[B - 1] += diff

    # 실제 배열에서 swap
    arr[i], arr[j] = arr[j], arr[i]

    # 위치 배열도 같이 갱신
    pos[A], pos[B] = j, i

print(*cnt_lst)
