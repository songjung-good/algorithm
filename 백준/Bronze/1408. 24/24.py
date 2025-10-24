
H1, M1, S1 = map(int, input().split(':'))
H2, M2, S2 = map(int, input().split(':'))
H, M, S = 0, 0, 0
if S1 <= S2:
    S = S2 - S1
else:
    S = S2 - S1 + 60
    M2 -= 1

if M1 <= M2:
    M = M2 - M1
else:
    M = M2 - M1 + 60
    H2 -= 1

if H1 <= H2:
    H = H2 - H1
else:
    H = H2 - H1 + 24

if H == 0:
    print('00', end=':')
elif H < 10:
    print('0' + str(H), end=':')
else:
    print(H, end=':')
if M == 0:
    print('00', end=':')
elif M < 10:
    print('0' + str(M), end=':')
else:
    print(M, end=':')
if S == 0:
    print('00')
elif S < 10:
    print('0' + str(S))
else:
    print(S)