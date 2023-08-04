T = int(input())

for tc in range(1, T+1):        #case 번호
    card_line = int(input())    #주어지는 카드 장수
    card_num = int(input())     #

    max_num = 0
    min_num = 10

    for i in range(card_line):
        A = card_num % (10 ** (i+1))
        if A > max_num:
            max_num = A
        if A < min_num:
            min_num = A
        card_num -= A(10 ** (i))
        A