def solution(A, B):
    answer = 0
    num = len(A)
    new_A = A

        
    while answer < num:
        if new_A == B:
            break
        new_A = new_A[-1] + new_A[:num-1]
        answer += 1
    if answer >= num:
        answer = -1
    return answer