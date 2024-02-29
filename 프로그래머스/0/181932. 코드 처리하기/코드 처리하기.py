def solution(code):
    answer = ''
    mode = 0
    num = 0
    
    for idx in code:
        if mode == 0:
            if idx == '1':
                mode = 1
            else:
                if num % 2 == 0:
                    answer += idx
        else:
            if idx == '1':
                mode = 0
            else:
                if num % 2 == 1:
                    answer += idx
        num += 1
        
    if answer == '':
        answer = "EMPTY"
        
    return answer