import sys
input = sys.stdin.readline

N = int(input())
A_lst = list(map(int,input().split()))
B_lst = list(map(int, input().split()))
DRAW = [(1,1), (2,2), (3,3)]
A_win = [(1,3), (2,1), (3,2)]
B_win = [(1,2), (2,3), (3,1)]

past = 0
cnt = 0
ans = 0

for n in range(N):
    A, B = A_lst[n], B_lst[n]
    if (A, B) in DRAW:
        if past:
            past = 0
        else:
            past = 1
        if ans < cnt:
            ans = cnt
        cnt = 1
    elif (A, B) in A_win:
        if past:
            if ans < cnt:
                ans = cnt
            past = 0
            cnt = 1
        else:
            cnt += 1
    else:
        if past:
            cnt += 1
        else:
            if ans < cnt:
                ans = cnt
            past = 1
            cnt = 1

if ans < cnt:
    ans = cnt
print(ans)