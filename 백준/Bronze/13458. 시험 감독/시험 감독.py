# 교실 수
N = int(input())
# 교실 별 응시자 수
A = list(map(int, input().split()))
# 정 감독, 부 감독
B, C = map(int, input().split())

# 필요한 감독 수
ans = 0

# 각 교실 별 응시자 수를 반복하면서 필요한 감독 수를 계산
for num_students in A:
    # 정감독관은 반드시 한 명 필요하므로 한 명 추가
    ans += 1
    # 남은 응시자 수에서 정감독관이 감시할 수 있는 인원을 뺀다.
    num_students -= B
    # 부감독관이 필요한 경우
    if num_students > 0:
        # 부감독관의 수를 계산하고 필요한 감독 수에 추가
        ans += num_students // C
        # 남은 응시자가 부감독관의 감시 인원보다 적으면 부감독관 한 명이 더 필요함
        if num_students % C != 0:
            ans += 1

print(ans)
