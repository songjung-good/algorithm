def solution(names):
    answer = []
    num = len(names)
    for i in range(0,num,5):
        answer.append(names[i])
    return answer