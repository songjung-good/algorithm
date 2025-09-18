def solution(wallet, bill):
    answer = 0
    if wallet[0] < wallet[1]:
        wallet[0], wallet[1] = wallet[1], wallet[0]
    while True:
        if bill[0] < bill[1]:
            bill[0], bill[1] = bill[1], bill[0]
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            break
        else:
            bill[0], bill[1] = bill[0] // 2, bill[1]
            answer += 1

    return answer