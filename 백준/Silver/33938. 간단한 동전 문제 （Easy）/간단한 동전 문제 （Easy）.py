def find_one_coin(num):
    if num == 0:
        return 0 if M == 0 else -1
    if M % num:
        return -1
    x = M // num
    return x if x >= 0 else -1

def find_two_coin(A, B):
    if A == 0 and B == 0:
        return 0 if M == 0 else -1
    if A == 0:
        return find_one_coin(B)
    if B == 0:
        return find_one_coin(A)

    max_cnt = float('inf')

    for A_cnt in range(2000):
        now = M - A_cnt * A
        if now % B != 0:
            continue

        B_cnt = now // B
        if B_cnt < 0:
            continue

        cnt = A_cnt + B_cnt
        if max_cnt > cnt:
            max_cnt = cnt

    return max_cnt if max_cnt != float('inf') else -1
    
N, M = map(int, input().split())
if N == 0:
    print(0 if M == 0 else -1)
elif N == 1:
    print(find_one_coin(int(input())))
else:
    A_coin, B_coin = map(int, input().split())
    print(find_two_coin(A_coin, B_coin))