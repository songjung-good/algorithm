def solution(num_list):
    answer = num_list
    A = num_list[-1]
    B = num_list[-2]
    if A > B:
        C = A - B
    else:
        C = A * 2
    answer.append(C)
    
    return answer