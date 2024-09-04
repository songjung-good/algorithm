A, B = map(int, (input().split()))

A_lst = [A, ]
B_lst = [B, ]
A_num = 1
B_num = 1
check = 0
while True:
    if A_lst[-1] == B_lst[-1]:
        break
    elif A_lst[-1] < B_lst[-1]:
        A_num = A_num + 1
        A_lst.append(A * A_num)
    elif A_lst[-1] > B_lst[-1]:
        B_num = B_num + 1
        B_lst.append(B * B_num)

print(A_lst[-1])