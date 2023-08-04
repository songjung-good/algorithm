'''
# A, B가 책의 쪽수 탐색
# 왼쪽 l 오른쪽 r 중간 c = int((l+r) / 2)
# c와 찾는 쪽이 같으면 중단
# A와 B 둘 중 빨리 찾는 쪽은?
'''



'''
    #1 따로 탐색
'''
'''
T = int(input())                    # T는 case 수
P, A, B = map(int, input().split()) # P는 책의 쪽 수, A의 목표점, B의 목표점

for tc in range(1, T+1):

    mid_A = int(P / 2)
    mid_B = int(P / 2)
    min_A = P//4
    min_B = P//4
    count_A = 0
    count_B = 0

    while mid_A != A:
        min_A = min_A//2
        if mid_A > A:       # 중간 값이 A의 목표보다 크면
            mid_A -= min_A
        elif mid_A < A:
            mid_A += min_A
        count_A += 1

    while mid_B != B:
        min_B = min_B // 2
        if mid_B > B:       # 중간 값이 A보다 크면
            mid_B -= min_B
        elif mid_B < B:
            mid_B += min_B
        count_B += 1

    if count_A > count_B:
        print(f'#{tc} A')
    elif count_A < count_B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
'''



'''
    #2 함수를 이용
'''
'''
T = int(input())                    # T는 case 수


def binary_search(ap, gol):
    left, right = 1, p  # 페이지 범위 설정
    count = 0  # 이동 횟수 초기화

    while left <= right:
        mid = (left + right) // 2  # 중간 페이지 계산
        count += 1  # 이동 횟수 증가

        if mid == goal:  # 목표 페이지를 찾았으면 종료
            break
        elif mid < goal:  # 중간 페이지가 목표 페이지보다 작으면 오른쪽 구간으로 이동
            left = mid 
        else:  # 중간 페이지가 목표 페이지보다 크면 왼쪽 구간으로 이동
            right = mid 

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

'''


'''
    #3 
    책의 중심점 p//2
    A의 이진수와 (B-p//2)를 해서 1의 수가 더 작은 걸 출력 
'''
'''
T = int(input())                        # T는 case 수
P, A, B = map(int, input().split())     # P는 페이지, A의 목표점, B의 목표점

def binary(p, a):
    ans = 0
    if a > (p // 2):
        low_a = a - (p//2)
        while low_a > 2:
            low_a // 2
            if low_a % 2 == 1:
                ans += 1
            else:
                pass
    elif a < (p // 2):
        while a > 2:
            a // 2
            if a % 2 == 1:
                ans += 1
    else:
'''

