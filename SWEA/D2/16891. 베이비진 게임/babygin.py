#1
'''
def check_run(lst):
    # 같은 수 3개
    lst.sort()
    past = 0
    cnt = 0
    for i in lst:
        if i == past:
            cnt += 1
        else:
            past = i
            cnt = 1
        if cnt == 3:
            return 'Y'
    return 'N'


def check_triplet(lst):
    # 연속 수 3개
    lst.sort()
    stack = [lst[0]]
    i = 0
    j = len(lst)
    cnt_T = 1
    while i != j:
        if stack[-1] == lst[i]:
            pass
        elif stack[-1] + 1 == lst[i]:
            stack.append(lst[i])
            cnt_T += 1
            if cnt_T == 3:
                return 'Y'
        elif stack[-1] + 1 != lst[i]:
            stack.append(lst[i])
            cnt_T = 1
        i += 1
    return 'N'  # 연속 수 3개가 아닌 경우


T = int(input())
for tc in range(1, T+1):
    deck = list(map(int, input().split()))
    player1 = []
    player2 = []
    ans = 0

    #카드가 12개
    for i in range(12):
        #참가자가 3장 받기 전
        if i < 4:
            if i % 2 == 0:
                player1.append(deck[i])
            else:
                player2.append(deck[i])
        #참가자가 3장
        else:
            if i % 2 == 0:
                player1.append(deck[i])
                if check_run(player1) == 'Y' or check_triplet(player1) == 'Y':
                    ans = 1
                    break

            else:
                player2.append(deck[i])
                if check_run(player2) == 'Y' or check_triplet(player2) == 'Y':
                    ans = 2
                    break

    print(f'#{tc} {ans}')
'''

#2 카운트 정렬 이용
def check_babygin(lst):
    # 같은 수 3개
    cnt = 0
    for i in lst:
        if i == 3:
            return 'Y'
        elif i >= 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return 'Y'
    return 'N'

T = int(input())
for tc in range(1, T+1):
    deck = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    ans = 0

    #카드가 12개
    for i in range(12):
        #참가자가 3장 받기 전
        if i < 4:
            if i % 2 == 0:
                player1[deck[i]] += 1
            else:
                player2[deck[i]] += 1
        #참가자가 3장
        else:
            if i % 2 == 0:
                player1[deck[i]] += 1
                if check_babygin(player1) == 'Y':
                    ans = 1
                    break

            else:
                player2[deck[i]] += 1
                if check_babygin(player2) == 'Y':
                    ans = 2
                    break

    print(f'#{tc} {ans}')