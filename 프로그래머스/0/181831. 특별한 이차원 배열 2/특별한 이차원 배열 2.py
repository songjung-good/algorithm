def solution(arr):
    answer = 1
    N = len(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] != arr[j][i]:
                answer = 0
    return answer