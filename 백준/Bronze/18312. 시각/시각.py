'''
이코테 구현파트
예제 4-2
'''

N, K = map(str, input().split())
cnt = 0
for h in range(int(N)+1):
    if h < 10:
        H = '0' + str(h)
    else:
        H = str(h)
    for m in range(60):
        if m < 10:
            M = '0' + str(m)
        else:
            M = str(m)
        for s in range(60):
            if s < 10:
                S = '0' + str(s)
            else:
                S = str(s)
            if K in H + M + S:
                cnt += 1

print(cnt)
