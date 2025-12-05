def solution(strArr):
    arr = [0] * 31
    for s in strArr:
        arr[len(s)] += 1
    
    answer = max(arr)
    return answer