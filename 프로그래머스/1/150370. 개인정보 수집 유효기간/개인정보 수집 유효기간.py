def solution(today, terms, privacies):
    answer = []    
    Y, M, D = int(today[:4]), int(today[5:7]), int(today[8:])
    date = D + M * 28 + Y * 12 * 28
    dict = {}
    for t in terms:
        k, v = t.split(' ')
        dict[k] = int(v)
    
    cnt = 1
    for p in privacies:
        pri = p.split(' ')
        # 유효기간
        gap = dict[pri[1]] * 28
        # 수집일자
        Y_1, M_1, D_1 = pri[0].split('.')
        num = int(Y_1) * 28 * 12 + int(M_1) * 28 + int(D_1) + gap
        
        print(num, date)
        if num <= date:
            answer.append(cnt)
        
        cnt += 1
        
    return answer