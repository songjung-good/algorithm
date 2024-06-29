A, B = map(int, input().split())
print(A // B, end = '.')
C = A % B
cnt = 0
while C != 0:
    D = C*10 // B
    print(D, end = '')
    C = C*10 % B
    cnt += 1
    if cnt >= 1001:
        break