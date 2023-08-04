#1
for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        if lst[i] > lst[i - 2] and lst[i] > lst[i - 1] and lst[i] > lst[i + 1] and lst[i] > lst[i + 2]:
            new_lst = [lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2]]
            for k in range(0, 3):
                for j in range(0, 3-k):
                    if new_lst[j] > new_lst[j + 1]:
                        new_lst[j], new_lst[j + 1] = new_lst[j + 1], new_lst[j]

            ans += lst[i] - new_lst[-1]

    print(f'#{tc} {ans}')


# N은 건물 수
# lst는 건물의 높이(공터포함)
# 건물i 에서 (i-2) (i-1) 0 (i+1) (i+2)와 비교
# i가 제일 크면 i와 그 다음 큰 수와의 차이를 저장
# 그 수의 합을 출력


# 2
for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(2, N-2):
        view = []
        if lst[i] > lst[i - 2] and lst[i] > lst[i - 1] and lst[i] > lst[i + 1] and lst[i] > lst[i + 2]:
            view.append(lst[i] - lst[i-2])
            view.append(lst[i] - lst[i-1])
            view.append(lst[i] - lst[i+1])
            view.append(lst[i] - lst[i+2])

            # for k in range(0, 3):
            #     for j in range(0, 3-k):
            #         if new_lst[j] > new_lst[j + 1]:
            #             new_lst[j], new_lst[j + 1] = new_lst[j + 1], new_lst[j]
            #
            # ans += lst[i] - new_lst[-1]

    print(f'#{tc} {ans}')



#3
for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        if lst[i-2] > lst[i] or lst[i-1] > lst[i]:
            continue
        if lst[i+2] > lst[i] or lst[i+1] > lst[i]:
            continue
        MAX = max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])



#4
for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N - 2):
        max_apt = lst[i-2]
        for j in range(i-1, i+3):
            if j == i:
                continue
            else:
                if max_apt < j:
                    max_apt = j
        for lst[i] > max_apt:
