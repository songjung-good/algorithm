def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        for i in range(a, b+1):
            answer.append(arr[i])
    return answer