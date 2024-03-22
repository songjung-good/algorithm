def solution(arr):
    answer = []
    now = -1
    for i in arr:
        if now != i:
            answer.append(i)
            now = i
        else:
            pass
    return answer