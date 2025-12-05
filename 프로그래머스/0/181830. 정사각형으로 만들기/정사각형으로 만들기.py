def solution(arr):
    answer = [[]]
    A, B = len(arr), len(arr[0])
    cnt = abs(A - B)
    if A > B:
        for i in arr:
            for c in range(cnt):
                i.append(0)
    else:
        lst = [0] * B
        for c in range(cnt):
            arr.append(lst)
                
    return arr