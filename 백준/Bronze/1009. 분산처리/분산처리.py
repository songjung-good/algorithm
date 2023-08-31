T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a % 10 == 1:
        print(1)
    elif a % 10 == 2:
        two_lst = [6, 2, 4, 8]
        print(two_lst[(b) % 4])
    elif a % 10 == 3:
        three_lst = [1, 3, 9, 7]
        print(three_lst[(b) % 4])
    elif a % 10 == 4:
        four_lst = [6, 4]
        print(four_lst[(b) % 2])
    elif a % 10 == 5:
        print(5)
    elif a % 10 == 6:
        print(6)
    elif a % 10 == 7:
        seven_lst = [1, 7, 9, 3]
        print(seven_lst[(b) % 4])
    elif a % 10 == 8:
        eight_lst = [6, 8, 4, 2]
        print(eight_lst[(b) % 4])
    elif a % 10 == 9:
        nine_lst = [1, 9]
        print(nine_lst[(b) % 2])
    elif a % 10 == 0:
        print(10)