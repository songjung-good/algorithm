'''
T = int(input())
for tc in range(1, 1+T):
    ans = 0                 #문자열 B가 사용된 횟수
    A, B = input().split()      #문자열 A, B를 받는다.
    num_A, num_B = len(A), len(B)   #A와 B의 길이

    index_A = 0                 #문자열 i의 인덱스
    while index_A < num_A:      #index_A가 문자열 A의 길이보다 작으면 반복
        index_B = 0             #문자열 B의 인덱스
        while index_B < num_B:  #index_B 가 B의 길이보다 작으면 반복
            try:
                if A[index_A + index_B] != B[index_B]:
                    index_A += index_B + 1
                    ans += index_B + 1
                    break
            except IndexError:
                index_A += index_B + 1
                ans += index_B
                break
            index_B += 1

        if index_B >= num_B:
            index_A += num_B
            ans += 1

    print(f'#{tc} {ans}')


'''

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()  # 입력받은 문자열 A, B
    len_A, len_B = len(A), len(B) #문자열 A와 B의 길이

    ans = 0                 #타이핑을 몇 번 하는지
    index_A = 0             #A의 시작 위치

    while index_A < len_A:  #A의 길이보다 인덱스의 길이가 작으면
        match = True        #맞으면 True 반환
        for i in range(len_B):  #B의 길이만큼 순환
            if index_A + i >= len_A or A[index_A + i] != B[i]: #A의 길이를 초과하거나 B의 문자와 안맞으면
                match = False   #False 반환
                break

        if match:  # 문자열 B와 일치하면 B의 길이만큼 건너뛴다
            ans += 1
            index_A += len_B
        else:
            ans += 1
            index_A += 1

    print(f'#{tc} {ans}')
