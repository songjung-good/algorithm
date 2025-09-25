def solution(binomial):
    answer = 0
    lst = binomial.split()
    if lst[1] == '+':
        answer = int(lst[0]) + int(lst[2])
    elif lst[1] == '-':
        answer = int(lst[0]) - int(lst[2])
    elif lst[1] == '*':
        answer = int(lst[0]) * int(lst[2])
    return answer