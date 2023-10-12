# 버스정류장 1 ~ 5000
# 버스 노선 N개
# i번째 버스노선은 번호 Ai이상 bi이하인 모든 정류장 다님
# P개의 버스 정류장에 각 정류장에 몇개의 버스노선이 다니는지

# 버스는 0 -> N번 정류장 충전시 K만큼 이동가능
# 운행완료 못하면 0

#버스가 한칸 이동하면 (k-1), (N-1)
#버스가 a칸 이동 (k-a), (N-a)


#1 충전기 기준(최종지점 없음)
T = int(input())            #T는 노선수

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #K는 버스최대이동거리 N은 정류장수 M은 충전기 수
    charge_station = list(map(int, input().split()))
    stay_station = 0

    for i in range(0, M):
        if K - charge_station[i] >= 0:
            bus_gauge = (K - charge_station[i]) - (charge_station[i+1] - charge_station[i])
            if bus_gauge < 0:
                bus_gauge += K
                stay_station += 1
            else:

                continue
        else:
            stay_station = 0
            break

    print(f'#{tc} {stay_station}')

        # 버스가 충전소에 도착할때
        #  (남은 이동수 - 다음 충전소거리) >= 0 지나친다
        #   남은이동수 - 다음충전소거리 <0 충전한다.(충전 + 1)


#2 버스를 한 칸씩 전진
T = int(input())            #T는 노선수

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #K는 버스최대이동거리 N은 정류장수 M은 충전기 수
    charge_station = list(map(int, input().split()))
    goal = N

    for i in range(0, M):
        if  >


#3 갈 수 있는 거리 내에 가장 먼 충전소
T = int(input())            #T는 노선수

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #K는 버스최대이동거리 N은 정류장수 M은 충전기 수
    stations = list(map(int, input().split()))

    now = 0
    cnt = 0
    next_D = now + K  # 3 10 5 -> now = 0, cnt = 0, 다음목적지 : now + K -> 3

#for문은 순회하는 횟수를 알때 유리
#whlie문은 종료조건을 알면 사용

    while next != N:
        if next in stations:
            cnt += 1
            now = next      # now가 K으로 재할당됨
            next = now + K
        else:
            next -= 1

        if next == now:     #버스 가용 거리 내에 충전기가 없는 경우
            cnt = 0
            break

        print(f'#{t} {cnt}')







