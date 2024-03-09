def bi_num(now, n):
    number = now
    binum = ''
    cnt = 0
    while cnt != n:
        if number == 0:
            binum = '0' + binum
        elif number % 2 == 1:
            binum = '1' + binum
        else:
            binum = '0' + binum
        number = number // 2
        cnt += 1
    return binum

def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        bi1 = bi_num(num1, n)
        bi2 = bi_num(num2, n)
        neomap = ""
        for b1, b2 in zip(bi1, bi2):
            if b1 == b2 == '0':
                neomap += ' '
            elif b1 == '1' or b2 == '1':
                neomap += '#'
        answer.append(neomap)
    return answer
