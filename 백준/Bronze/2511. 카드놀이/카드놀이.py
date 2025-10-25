A_lst = list(map(int,input().split()))
B_lst = list(map(int,input().split()))
last_win = 0
A_score = 0
B_score = 0

for i in range(10):
    A, B = A_lst[i], B_lst[i]
    if A > B:
        A_score += 3
        last_win = 1
    elif A < B:
        B_score += 3
        last_win = 2
    else:
        A_score += 1
        B_score += 1

print(A_score, B_score)
if A_score > B_score:
    print('A')
elif A_score < B_score:
    print('B')
else:
    if last_win == 0:
        print('D')
    elif last_win == 1:
        print('A')
    else:
        print('B')