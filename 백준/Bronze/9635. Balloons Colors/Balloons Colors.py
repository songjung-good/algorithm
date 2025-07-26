T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    num_lst = list(map(int, input().split()))
    if num_lst[0] == X and num_lst[-1] == Y:
        print('BOTH')
    elif num_lst[0] == X and num_lst[-1] != Y:
        print('EASY')
    elif num_lst[0] != X and num_lst[-1] == Y:
        print('HARD')
    else:
        print('OKAY')