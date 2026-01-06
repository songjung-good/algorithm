from collections import deque

N = int(input())
Q1 = deque(list(map(int, input().split())))
Q2 = deque(list(map(int, input().split())))

checked = 0
c_click = 0
unchecked = 0
u_click = 0

for n in range(N):
    A, B = Q1[n], Q2[n]

    if A == 0:
        unchecked += 1
        if A != B:
            u_click += 1
    else:
        checked += 1
        if A != B:
            c_click += 1

if checked == 0:
    cnt = N - u_click + 1
    print(cnt if cnt <= u_click else u_click)
elif unchecked == 0:
    cnt = N - c_click + 1
    print(cnt if cnt <= c_click else c_click)
else:
    cnt_1 = c_click + unchecked - u_click + 1
    cnt_2 = u_click + checked - c_click + 2
    cnt_3 = c_click + u_click
    print(min(cnt_1, cnt_2, cnt_3))



'''
0. click 더하기
1. 만약 전체가 꺼져 있는 경우
    1. 전체 토글을 1번 눌려서 N - u_click만 더하기
2. 만약 전체가 켜져 있는 경우
    1. 전체 토글을 1번 눌려서 N - c_click만 더하기
3. 일부만 켜져 있는 경우
    1. 전체 토글을 1번 눌려서 기존 c_click만 더하기
    2. 전체 토글을 2번 눌려서 기존 u_click만 더하기
'''