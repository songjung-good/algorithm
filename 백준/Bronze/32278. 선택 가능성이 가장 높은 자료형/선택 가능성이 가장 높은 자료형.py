def find_type(n):
    if -32_768 <= n <= 32_767:
        print('short')
    elif -2_147_483_648 <= n <= 2_147_483_647:
        print('int')
    else:
        print('long long')

N = int(input())
find_type(N)