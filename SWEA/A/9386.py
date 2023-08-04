T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # arr = list(input()) #['1', '1', '0', '0', '1', '1', '1', '0']
    # arr = list(input().split('0')) #['', '', '11', '', '111', '']
    max_count = 0
    for i in range(N):
        if i