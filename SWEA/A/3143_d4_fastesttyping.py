
'''
T = int(input())
for tc in range(1, 1+T):
    ans = 0                 #타자 횟수

    A, B = input().split()  #A는 문자열 B는 단축어
    num_A, num_B = len(A), len(B)       #A의 길이 num_A, B의 길이 num_B

    i = 0                   #전체 문자열에서 진행위치 파악
    while i < num_A:        #A의 길이보다 진행 위치가 작으면 진행
        j = 0               #단축어의 현재 인덱스 번호
        while j < num_B:        #단축어의 인덱스보다 낮은상태면 진행
            if A[i+j] != B[j]:  #문자열에서 현재위치 i부터 j까지의 원소와 단축어의 원소 비교
                i += j+1        #다르면 문자열의 위치를 j+1만큼 이동
                ans += j+1  #타자횟수 j+1만큼 추가
                break       #while문 종료
            j += 1          #다르면 j에 1추가한다.
            if j+1+i == num_A:
                i += j+1
                ans += j+i
                break

        if j == num_B:               #단축 사용했으니까 +1
            i += num_B
            ans += 1

    # print(A, B)
    # print(num_B, num_A)
    print(f'#{tc} {ans}')
'''

'''
#2
T = int(input())
for tc in range(1, 1+T):
    ans = 0

    A, B = input().split()  #A는 문자열 B는 단축어
    num_A, num_B = len(A), len(B)       #

    i = 0
    while i <= num_A:
        j = 0
        while j < num_B:
            if A[i+j] != B[j]:
                i += j+1
                ans += j+1
                break
            j += 1
        if j > num_B:               #단축 사용했으니까 +1
            i += num_B
            ans += 1

    print(f'#{tc} {ans}')
    
'''

A, B = input().split()
num_A, num_B = len(A), len(B)

i = 0
while i < num_A:
    cnt = 0
    while cnt < num_B:
        try:
            if A[i+cnt] != B[cnt]:
                i += cnt+1
                ans += cnt+1
                break
        except IndexError:
            i += cnt + 1
            ans += cnt
            break
        cnt += 1

    if cnt >= num_B:
        i += num_B
        ans += 1

print(f'#{tc} {ans}')