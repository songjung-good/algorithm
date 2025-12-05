def solution(rank, attendance):
    answer = 0
    lst = []
    for i in range(len(rank)):
        if attendance[i]:
            lst.append((rank[i], i))
    lst.sort()
    answer += lst[0][1] * 10000 + lst[1][1] * 100 + lst[2][1]
    return answer