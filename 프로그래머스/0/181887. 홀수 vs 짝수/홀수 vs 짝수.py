def solution(num_list):
    ODD = 0
    EVEN = 0
    for i in range(len(num_list)):
        if i % 2:
            ODD += num_list[i]
        else:
            EVEN += num_list[i]
    answer = max(ODD, EVEN)
    return answer