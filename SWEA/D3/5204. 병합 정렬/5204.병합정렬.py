def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global count
    result = []
    left_idx, right_idx = 0, 0

    # 왼쪽 마지막 원소와 오른쪽 마지막 원소의 크기비교
    if left[-1] > right[-1]:
        count += 1

    # 한쪽 원소 다 사용할 때 까지 반복
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    # 남은 원소 리스트에 추가
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    # 정렬된 리스트 반환
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    count = 0
    sorted_lst = merge_sort(lst)
    ans = sorted_lst[N // 2]

    print(f'#{tc} {ans} {count}')