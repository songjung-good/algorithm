def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    dice.sort()
    a = dice[0]
    b = dice[1]
    c = dice[2]
    d = dice[3]
    
    if a == b:
        if b == c:
            if c == d:
                answer = 1111 * a
            else:
                answer = (10 * a + d) ** 2
        else:
            if c == d:
                answer = (a + c) * (c-a)
            else:
                answer = c * d
    else:
        if b == c:
            if c == d:
                answer = (10 * d + a)  ** 2
            else:
                answer = a * d
        else:
            if c == d:
                answer = a * b
            else:
                answer = a
    return answer