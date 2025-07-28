def solution(num_list, n):
    answer = []
    num = len(num_list)
    for i in range(0,num,n):
        answer.append(num_list[i])
    return answer