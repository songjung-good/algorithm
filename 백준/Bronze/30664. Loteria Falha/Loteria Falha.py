while True:
    N = int(input())
    if N == 0:
        exit()
    else:
        if N % 42:
            print('TENTE NOVAMENTE')
        else:
            print('PREMIADO')