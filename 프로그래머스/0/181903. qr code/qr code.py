def solution(q, r, code):
    answer = ''
    num = len(code) 
    for n in range(num):
        if n % q == r:
            answer += code[n]
    
    return answer