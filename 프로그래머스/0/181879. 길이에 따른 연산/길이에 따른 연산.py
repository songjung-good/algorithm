from functools import reduce
def solution(num_list):
    answer = 0
    A = len(num_list)
    if A >= 11:
        answer = sum(num_list)
    else:
        answer = reduce(lambda x, y: x * y, num_list)
    return answer