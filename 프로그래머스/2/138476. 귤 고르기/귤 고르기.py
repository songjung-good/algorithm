def solution(k, tangerine):
    answer = 0
    lst = [0] * 10_000_001
    
    for t in tangerine:
        lst[t] += 1
    
    lst.sort(reverse=True)
    
    for l in lst:
        k -= l
        answer += 1
        if k <= 0:
            break
    
    return answer