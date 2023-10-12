#1 상자의 높이별로 자료 정리 후 제일 작은것과 제일 많은 것 하나씩 이동
T = 10

for tc in range(1, T+1):
    room = [0 for i in range(0, 101)]  # 상자가 쌓인 방의 크기
    dump = int(input())                 # 덤프횟수
    data = list(map(int, input().split()))  # 상자높이 리스트

    min_box = 100
    max_box = 0

    for i in range(0, 100):
        room[data[i]] += 1          # box높이별로 자료정리
        if data[i] > max_box:
            max_box = data[i]
        if data[i] < min_box:
            min_box = data[i]

    # print(min_box, max_box)

    while dump > 0 and min_box < (max_box - 1): #dump횟수가 0 이거나 옮길 상자가 없으면 중단
        room[min_box] -= 1                      #제일 낮은 박스에서 그다음 낮은걸로 옮기기
        room[min_box + 1] += 1
        room[max_box] -= 1
        room[max_box - 1] += 1                  #제일 높은 박스에서 그다음 높은걸로 옮기기
        if room[min_box] == 0:
            min_box += 1
        if room[max_box] == 0:
            max_box -= 1
        dump -= 1

    # print(max_box, min_box)
    ans = max_box - min_box
    print(f'#{tc} {ans}')


# 2
T = 10

for tc in range(1, T+1):
    room = [0 for i in range(0, 101)]  # 상자가 쌓인 방의 크기
    dump = int(input())                 # 덤프횟수
    data = list(map(int, input().split()))  # 상자높이 리스트

    for i in range(dump):                   #덤프횟수만큼 반복
        max_index = data.index(max(data))
        min_index = data.index(min(data))
        data[max_index] -= 1                #최고값 숫자 내리고
        data[min_index] += 1                #최저값 숫자 올리기

    result = max(data) - min(data)

    print(f'#{tc} {result}')

#3
T = 10

for tc in range(1, T+1):
    room = [0 for i in range(0, 101)]  # 상자가 쌓인 방의 크기
    dump = int(input())                 # 덤프횟수
    data = list(map(int, input().split()))  # 상자높이 리스트

    data.sort()

    for _ in range(dump):
        data[0] += 1
        data[-1] -= 1
        data.sort()

    result = max(data) - min(data)

    print(f'#{tc} {result}')


#4
T = 10

for tc in range(1, T + 1):
    room = [0 for i in range(0, 101)]  # 상자가 쌓인 방의 크기
    dump = int(input())  # 덤프횟수
    data = sorted(list(map(int, input().split())))  # 상자높이 리스트

    for _ in range(dump):
        data[0] += 1
        data[-1] -= 1
        data.sort()

    result = max(data) - min(data)

    print(f'#{tc} {result}')