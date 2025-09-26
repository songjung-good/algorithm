def solution(array, commands):
    answer = []
    for now in range(len(commands)):
        i, j, k = commands[now]
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
    return answer