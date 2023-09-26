import sys
input = sys.stdin.readline

while True:
    num_lst = list(map(int, input().split()))
    num_lst.sort()
    if sum(num_lst) == 0:
        break
    check_num = []
    for i in num_lst:
        check_num.append(i**2)

    if check_num[0]+check_num[1] == check_num[2]:
        print('right')
    else:
        print('wrong')