M_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def find_day(y, m, d):
    y_prev = y - 1
    cnt_day = y_prev * 365 + (y_prev//4) - (y_prev//100) + (y_prev//400)

    cnt_day += sum(M_day[:m-1]) + d

    if m > 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            cnt_day += 1

    return cnt_day

Y_1, M_1, D_1 = map(int, input().split())
Y_2, M_2, D_2 = map(int, input().split())

e_point = find_day(Y_2, M_2, D_2)
s_point = find_day(Y_1, M_1, D_1)
o_point = find_day(Y_1+1000, M_1, D_1)

if o_point <= e_point:
    print('gg')
else:
    print(f'D-{e_point-s_point}')