from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A_lst = [int(input()) for _ in range(N)]
B_lst = [n for n in range(1, 2*N+1) if n not in A_lst]

A_deck = deque(sorted(A_lst))
B_deck = deque(sorted(B_lst))
A_cnt = N
B_cnt = N
card = 0
turn = 1

while A_deck and B_deck:
    now = 0
    deck = deque([])
    if turn:
        while A_deck:
            num=A_deck.popleft()
            if num > card:
                now = num
                break
            else:
                deck.append(num)
        card = now
        deck.extend(A_deck)
        A_deck = deck
        turn = 0
    else:
        while B_deck:
            num=B_deck.popleft()
            if num > card:
                now = num
                break
            else:
                deck.append(num)
        card = now
        deck.extend(B_deck)
        B_deck = deck
        turn = 1

print(len(B_deck))
print(len(A_deck))