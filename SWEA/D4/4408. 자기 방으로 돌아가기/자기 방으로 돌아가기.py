T = int(input())

for tc in range(1, 1+T):
    #이동하는 횟수 
    N = int(input())
    #복도
    corridor = [0] * 201
    #횟수만큼 반복
    for _ in range(N):
        #방 번호 X, Y
        X, Y = map(int, input().split())
        # 큰 수가 X로 나올 경우
        if X > Y:
            X, Y = Y, X
        #해당 복도를 지나는 횟수.
        for i in range((X+1)//2, (Y+1)//2 + 1):
            #만약 1번 방과 2번 방에서 앞은 1번복도   
            corridor[i] += 1

    max_time = max(corridor)
    # for i in range(201):
    #     if max_time < corridor[i]:
    #         max_time = corridor[i]

    print(f'#{tc} {max_time}')