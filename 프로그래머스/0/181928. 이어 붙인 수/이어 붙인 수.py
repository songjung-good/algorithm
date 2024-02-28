def solution(num_list):
    A = ''
    B = ''
    for i in num_list:
        if i % 2 == 1:
            A += str(i)
        else:
            B += str(i)
    answer = int(A) + int(B)
    return answer