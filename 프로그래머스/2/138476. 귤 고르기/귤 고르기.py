def solution(k, tangerine):
    answer = 0
    size = {}
    for i in tangerine:
        if i in size:
            size[i] = size[i] + 1
        else:
            size[i] = 1

    sorted_size = sorted(size.items(), key = lambda x: x[1], reverse=True)
    
    cnt = 0
    for s, c in sorted_size:
        answer += 1
        cnt += c
        if cnt >= k:
            break
        
    return answer