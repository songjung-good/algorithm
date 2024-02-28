def solution(num_list):
    answer = 0
    A = 1
    B = 0
    for i in num_list:
        A *= i
        B += i
    if A < B**2:
        answer = 1
    return answer