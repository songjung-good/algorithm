T = int(input())

# map (함수, 이터러블) : 함수를 이터러블한 자료에 하나하나 적용

for tc in range(1, T+1):
    room_size = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    ans1 = 0
    for j in range(room_size):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            ans += 1
        elif lst[j] <= lst[j+1]:
            lst[-1] = lst[j]
            if ans1 > ans:
                ans = 0
            elif ans1 < ans:
                ans1 = ans
                ans = 0

    print(f'#{tc} {ans1}')  # T는 케이스 숫자  두번째 {}는 답