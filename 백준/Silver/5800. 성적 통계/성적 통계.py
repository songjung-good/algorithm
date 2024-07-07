# K는 반의 수
K = int(input())
for i in range(K):
    CLASS = list(map(int, input().split()))
    # 학생 수
    A = CLASS.pop(0)
    CLASS.sort(reverse=True)
    # 최소 최대 차이 구하기
    MAX = max(CLASS)
    MIN = min(CLASS)
    max_gap = 0
    for z in range(1, A):
        GAP = CLASS[z - 1] - CLASS[z]
        if max_gap < GAP:
            max_gap = GAP

    print(f'Class {i+1}')
    print(f'Max {MAX}, Min {MIN}, Largest gap {max_gap}')