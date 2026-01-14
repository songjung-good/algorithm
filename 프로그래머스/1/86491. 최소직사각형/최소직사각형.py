def solution(sizes):
    r, l = 0, 0
    for size in sizes:
        A, B = min(size), max(size)
        r, l = max(A, r), max(B, l)
    answer = r*l
    return answer