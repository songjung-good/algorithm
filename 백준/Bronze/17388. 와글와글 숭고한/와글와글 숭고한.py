S, K, H = map(int, input().split())
A = sum([S, K, H])
if A >= 100:
    print('OK')
else:
    if S < K and S < H:
        print('Soongsil')
    elif K < S and K < H:
        print('Korea')
    else:
        print('Hanyang')