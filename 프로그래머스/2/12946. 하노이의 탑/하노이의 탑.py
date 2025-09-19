def hanoi(n, start, mid, end, a):
    if n == 1:
        a.append([start, end])
    else:
        hanoi(n-1, start, end, mid, a)
        a.append([start, end])
        hanoi(n-1, mid, start, end, a)

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
        
    return answer