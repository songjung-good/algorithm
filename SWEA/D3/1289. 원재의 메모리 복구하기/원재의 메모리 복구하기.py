T = int(input())

A = ['0', '1']
for tc in range(1, T+1):
    cnt = 0
    correct = str(input())
    for i in correct:
        if i != A[cnt%2]:
            cnt += 1
            
    print(f'#{tc} {cnt}')
            
    