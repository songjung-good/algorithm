'''
    출발점 0, 도착점 99
    방향 고정, 한개의 정점에는 최대 2개의 길
    0에서 99로 가는 길이 있으면 1 출력, 없으면 0 출력

    테스트의 번호와 길의 개수
    순서쌍

    최대 2개의 길이므로 2개의 스택 생성
    99번에서 0번 가는 길 탐색
'''
#1 뒤로 탐색
'''

for _ in range(10):
    tc, N = map(int, input().split())

    stack_1 = [0] * 99
    stack_2 = [0] * 99
    goal_1 = 0
    goal_2 = 0

    lst = list(map(int, input().split()))
    for i in range(N):
        start_dot = lst[i * 2]
        if stack_1[start_dot] == 0:
            stack_1[start_dot] = lst[i * 2 + 1]
        else:
            stack_2[start_dot] = lst[i * 2 + 1]
        if lst[i * 2 + 1] == 99:
            if goal_1 != 0:
                goal_2 = i
            else:
                goal_1 = i

    ans = 0
    while N > 0:
        # if goal_1 == 0 and goal_2 == 0:
        #     break


        else:


    print(f'#{tc} {ans}')
'''
#2 앞으로 탐색
'''
    arr_1[0] = X arr_2[0] = Y에서 움직일 수 있는 방향 X 확인 arr_1[X], arr_2[X]
    1) arr_1[X], arr_2[X] 둘 다 0이면
        arr_1[0] = 0, arr_1[Y], arr_2[Y] 탐색
    2) arr_1[X], arr_2[X] 둘 다 길이면,
        arr_2로 이동하고 arr_1[x]를 저장
    3) 한 쪽 만 길이면,
        저장하지않고 지나온 길은 0으로 변경
        
'''
for _ in range(10):
    tc, N = map(int, input().split())

    arr_1 = [0] * 100            #0번 노드 부터 99번 노드 까지 만든다.(98까지 만들어도 무관)
    arr_2 = [0] * 100

    lst = list(map(int, input().split()))   #간선(edge)의 방향
    for i in range(N):
        start_dot = lst[i * 2]              #출발점(각 정점 당 간선은 최대 2개)
        if arr_1[start_dot] == 0:           #arr_1이 비어있으면 넣고
            arr_1[start_dot] = lst[i * 2 + 1]
        else:
            arr_2[start_dot] = lst[i * 2 + 1]   #arr_1이 채워져있으면 arr_2

    ans = 0     #99번 까지 도달하는지
    top = 0     #
    stack = [0] * N

    # 심플하게 생각하면 그냥 숫자따라 가다가 막히면 2번 배열을
    while N > 0:    #간선을 다 이용하면 탈출
        if arr_1[stack[top]] == 99 or arr_2[stack[top]] == 99:
            ans = 1     #99번 방향의 간선 찾으면 탈출
            break
        elif top == -1:
            break

        if arr_1[stack[top]] != 0:

            N -= 1                          #간선 하나 사용
            top += 1                        #stack 위치 이동
            stack[top] = arr_1[stack[top-1]]  #arr_1의 방향 저장
            arr_1[stack[top-1]] = 0     #지나간 다리 소모
        elif arr_2[stack[top]] != 0:

            N -= 1
            top += 1
            stack[top] = arr_2[stack[top-1]]
            arr_2[stack[top-1]] = 0
        else:
            top -= 1

    print(f'#{tc} {ans}')