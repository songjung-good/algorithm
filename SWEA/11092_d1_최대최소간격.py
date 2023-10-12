T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 #최솟값의 인덱스
    max_idx = 0 #최대값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i

    m_ans = max_idx - min_idx
    if m_ans < 0:
        ans = m_ans * -1
    else:
        ans = m_ans

    print(f'#{tc} {ans}')
