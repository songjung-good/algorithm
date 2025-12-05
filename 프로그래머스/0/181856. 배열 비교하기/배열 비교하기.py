def solution(arr1, arr2):
    answer = 0
    A, B = len(arr1), len(arr2)
    if A > B:
        answer = 1
    elif A < B: 
        answer = -1
    else:
        C, D = sum(arr1), sum(arr2)
        if C > D:
            answer = 1
        elif C < D:
            answer = -1
    return answer