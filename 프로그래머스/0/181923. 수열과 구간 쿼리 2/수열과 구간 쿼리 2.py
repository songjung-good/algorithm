def solution(arr, queries):
    answer = []
    for [s, e, k] in queries:
        num = 1000001
        for i in arr[s:e+1]:
            if i > k and i < num:
                num = i
        if num == 1000001:
            answer.append(-1)
        else:
            answer.append(num)
    return answer