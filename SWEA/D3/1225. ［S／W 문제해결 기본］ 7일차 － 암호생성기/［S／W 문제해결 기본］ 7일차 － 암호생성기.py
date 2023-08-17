'''
    8개의 숫자를 입력 받는다.

    한 사이클
    첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
    다음 첫 번째 수는 2 감소한 뒤 맨 뒤
    다음 첫 번째 수는 3을 감소하고 맨 뒤
    다음 수는 4, 그 다음 수는 5를 감소

    숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료
'''

for tc in range(1, 11):
    input()
    cQsize = 8
    cQ = list(map(int, input().split()))
    front = 0
    rear = 7

    while front == 0:
        for i in range(5):
            cQ[front] = cQ[front] - (i+1)
            cQ.append(cQ.pop(front))
            if cQ[rear] <= 0:
                cQ[rear] = 0
                front = 1
                break

    print(f'#{tc}', *cQ)