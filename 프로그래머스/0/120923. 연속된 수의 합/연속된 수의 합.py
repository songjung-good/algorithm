def solution(num, total):
    answer = []
    e=total//num + num//2
    s=e-num+1
    for i in range(num):
        answer.append(s+i)
    return answer