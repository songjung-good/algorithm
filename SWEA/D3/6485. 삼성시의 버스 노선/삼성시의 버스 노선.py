'''
1 ~ 5000개의 정류장
노선 N개
i번째 노선은 Ai ~ Bi 정류장
P개의 정류장

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.

다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.

다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.

다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다


'''
# def bus_num(stop_num):
#     for i in range(N):
#         bus_stop[route[i][0]:route[i][1]] += 1
#
#     return bus_stop[stop_num]


T = int(input())
for tc in range(1, T+1):
    ans = []
    bus_stop = [0] * 5001
    #다니는 버스의 수
    N = int(input())
    #버스가 다니는 정류장 범위
    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            bus_stop[j] += 1

    #정류장 수
    p = int(input())
    #정류장 번호
    for _ in range(p):
        ans.append(bus_stop[int(input())])

    print(f'#{tc} {" ".join(map(str, ans))}')