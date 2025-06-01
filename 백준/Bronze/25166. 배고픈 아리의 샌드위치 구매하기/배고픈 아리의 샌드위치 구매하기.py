S, M = map(int, input().split())
coogie = [0] * 11
cnt = -1
while M:
    if M % 2:
        coogie[cnt] += 1
    else:
        pass
    M = M // 2
    cnt -= 1

charge = S - 1023
if charge <= 0:
    print('No thanks')
else:
    cnt = -1
    while charge:
        if charge % 2:
            if not coogie[cnt]:
                print('Impossible')
                exit()
        charge = charge // 2
        cnt -= 1
    print('Thanks')