def solution(arr):
    answer = []
    cnt = 0
    num = len(arr)
    while 2 ** cnt < num:
        cnt += 1
    for _ in range(2 ** cnt - num):
        answer.append(0)
    
    return arr + answer