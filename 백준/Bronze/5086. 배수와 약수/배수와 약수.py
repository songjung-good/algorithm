while True:
    M, N = map(int, input().split())
    if M == N:
        break
    elif M > N and M % N == 0:
        print('multiple')
    elif M < N and N % M == 0:
        print('factor')
    else:
        print('neither')


