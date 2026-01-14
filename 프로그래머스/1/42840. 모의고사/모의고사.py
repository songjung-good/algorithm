def solution(answers):
    from collections import deque
    A = deque([1, 2, 3, 4, 5])
    B = deque([2, 1, 2, 3, 2, 4, 2, 5])
    C = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    res = [0, 0, 0]
    for a in answers:
        if a == A[0]:
            res[0] += 1
        if a == B[0]:
            res[1] += 1
        if a == C[0]:
            res[2] += 1
        A.rotate(-1)
        B.rotate(-1)
        C.rotate(-1)
        
    num = max(res)
    ans = []
    for idx, r in enumerate(res):
        if r == num:
            ans.append(idx+1)
    
    return ans