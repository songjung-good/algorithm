def solution(numlist, n):
    answer = []
    lst = []
    for i in range(len(numlist)):
        num=numlist[i]
        lst.append((num, abs(num-n)))
    
    lst.sort(key=lambda x: (x[1], -x[0]))

    for j in range(len(lst)):
        answer.append(lst[j][0])
    return answer