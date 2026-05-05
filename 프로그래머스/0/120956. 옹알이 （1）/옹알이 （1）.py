def solution(babbling):
    answer = 0
    for b in babbling:
        e = len(b)
        s = 0
        while s < e:
            if b[s:s+2] == "ye":
                s+=2
            elif b[s:s+2] == "ma":
                s+=2
            elif b[s:s+3] == "aya":
                s+=3
            elif b[s:s+3] == "woo":
                s+=3
            else:
                break
        if s == e:
            answer += 1
                
            
    return answer