'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = [0] * 5001

    for i in range(P):
'''


T = int(input())                #테스트 케이스 수
for tc in range(1, 1+T):
    N = int(input())            #버스 노선 수
    bus_stop = [0] * 5001       #버스노선 5000개에 0

    for _ in range(N):
        Ai, Bi = map(int, input().split())  #i번째 버스 노선이 다니는 루트 Ai~Bi
        for i in range(Ai, Bi+1):   #버스정류장에 오는 버스 기록
            bus_stop[i] += 1

    # P = int(input())            #출력할 버스정류장 수
    # ans = []
    # for _ in range(P):
    #     ans += bus_stop[]

    P = int(input())            #출력할 버스정류장 수
    an = [int(input()) for _ in range(P)]

    for a in range(p):
        ans[a]

    print(f'#{tc} {}')