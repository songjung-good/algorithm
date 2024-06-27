A, B = map(int, input().split())
cnt = 0
while A < 5 and B < 5:
    if cnt == 0:
        B += A
        cnt = 1
    else:
        A += B
        cnt = 0

if A >= 5:
    print('yj')
else:
    print('yt')