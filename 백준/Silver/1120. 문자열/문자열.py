A, B = input().split()
cnt_A, cnt_B = len(A), len(B)

min_gap = cnt_A
for i in range(cnt_B - cnt_A + 1):
    gap = 0
    for j in range(cnt_A):
        if A[j] != B[j+i]:
            gap+=1

    if min_gap > gap:
        min_gap = gap

print(min_gap)