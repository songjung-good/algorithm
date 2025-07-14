import sys
input = sys.stdin.readline

# N개의 주차공간, M대의 차량
N, M = map(int, input().split())
# 주차장소의 무게당 비용 cost, 차량의 무게 car_weight
cost = [int(input()) for _ in range(N)]
car_weight = [int(input()) for _ in range(M)]

# 주차장소 사용 차량
parking_lot = [0] * N
parking_cnt = N
wait_lst = []
wait_cnt = 0
# 수입
income = 0
# 출입내용
for _ in range(2*M):
    order = int(input())
    if order < 0:
        order = abs(order)
        out_car = parking_lot.index(order)
        parking_lot[parking_lot.index(order)] = 0
        parking_cnt += 1
        if wait_cnt:
            car = wait_lst.pop(0)
            wait_cnt -= 1
            parking_lot[out_car] = car
            income += cost[out_car] * car_weight[car - 1]
            parking_cnt -= 1
    else:
        if parking_cnt:
            for n in range(N):
                if parking_lot[n] == 0:
                    parking_lot[n] = order
                    income += cost[n] * car_weight[order-1]
                    break
            parking_cnt -= 1
        else:
            wait_lst.append(order)
            wait_cnt += 1
            
print(income)