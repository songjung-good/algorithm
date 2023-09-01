'''
트럭의 용량 보다 무게가 낮으면 ok
그 중 무게의 합이 더 크걸 저장
작은 무게의 트럭부터 짐 실어보자

'''
T = int(input())
for tc in range(1, T+1):
    #N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    item_weight = list(map(int, input().split()))
    truck_Volume = list(map(int, input().split()))

    truck_Volume.sort()
    item_weight.sort(reverse=True)
    load_list = []

    item_idx = []
    idx = 0
    #용량이 작은 트럭부터
    for truck in range(M):
        #용량이 큰 화물부터
        for container in range(N):
            #컨테이너가 트럭용량보다 가볍고,
            if item_weight[container] <= truck_Volume[truck] and container not in item_idx:
                idx = container
                item_idx.append(idx)
                load_list.append(item_weight[idx])
                break

    ans = sum(load_list)

    print(f'#{tc} {ans}')