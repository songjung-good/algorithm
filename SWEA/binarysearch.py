
def search_bi(P, G):
    start = 1
    end = P
    count = 0

    while start <= end:
        mid = (start + end) // 2
        count += 1

        if G == mid:
            return count

        elif G > mid:
            start = mid

        else:
            end = mid

    return count


T = int(input())                    # T는 case 수

for tc in range(1, T+1):
    book_page, A_G, B_G = map(int, input().split())

    cnt_A = search_bi(book_page, A_G)
    cnt_B = search_bi(book_page, B_G)

    if cnt_A == cnt_B:
        print(f'#{tc} 0')
    elif cnt_A > cnt_B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} A')

'''
    def binarySearch(lst, N, goal)  
                 #lst : 탐색할 리스트  N : 리스트 원소 수    goal : 목표점
    start = 0
    end = N -1
    count = 0
    
    while start <= end:
        mid = (start + end) // 2
        count += 1
        
        if lst[mid] == goal:
            return True
            
        elif lst[mid] > goal:
            end = mid - 1
            
        else:
            start = mid + 1
    return False
'''

'''
    임의의 정렬된 자료에서 원소 A를 탐색할때, 해당 자료의 중간 인덱스를 기준으로 왼쪽에 있는지 오른쪽에 있는지 확인한다. 해당 작업이 가능하기 위해서는 오름차순으로 정렬된 자료에만 적용이 가능하다. 
    해당 자료가 왼쪽에 있으면 기존의 왼쪽 시작점과 기존의 중간점에서 인덱스 -1 지점을 오른쪽 끝점으로 삼고 다시 중간 인덱스를 기준으로 탐색한다.

    - 정렬된 자료(중간에 삽입 또는 삭제가 발생하면 추가로 정렬)
    - 중간 인덱스를 기준으로 탐색
    - 목표점이 중간점 보다 크면 오른쪽 탐색
    - 시간 복잡도 O(log n)
'''