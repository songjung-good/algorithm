def solution(msg):
    answer = []
    w = {chr(idx + 64):idx for idx in range(1, 27)}
    length = len(msg)
    next_idx = 27
    
    start = 0
    while start < length:
        end = start + 1
        while end <= length and msg[start:end] in w:
            end += 1

        answer.append(w[msg[start:end-1]])
        
        if end <= length:
            w[msg[start:end]] = next_idx
            next_idx += 1
            
        start = end - 1
    return answer