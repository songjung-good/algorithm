def solution(arr):
    answer = []
    a = -1
    b = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            if a == -1:
                a = i
            else:
                b = i
    if a == -1:
        answer.append(-1)
    else:
        if b == -1:
            answer.append(2)
        else:
            for i in range(a, b+1):
                answer.append(arr[i])
    return answer