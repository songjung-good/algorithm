T = int(input())                    # T는 case 수

def binary_search(p, goal):
    left, right = 1, p  # 페이지 범위 설정
    count = 0  # 이동 횟수 초기화

    while left <= right:
        mid = (left + right) // 2  # 중간 페이지 계산
        count += 1  # 이동 횟수 증가

        if mid == goal:  # 목표 페이지를 찾았으면 종료
            break
        elif mid < goal:  # 중간 페이지가 목표 페이지보다 작으면 오른쪽 구간으로 이동
            left = mid + 1
        else:  # 중간 페이지가 목표 페이지보다 크면 왼쪽 구간으로 이동
            right = mid - 1

    if count > p:  # 목표 페이지를 찾지 못한 경우
        count = 0

    return count  # 이동 횟수 반환

for tc in range(1, T+1):
    P, A, B = map(int, input().split())  # P는 페이지, A의 목표점, B의 목표점

    count_A = binary_search(P, A)
    count_B = binary_search(P, B)

    if count_A < count_B:
        print(f'#{tc} A')
    elif count_A > count_B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
