# 입력 값
N = int(input())
# 새의 수, 시간 설정
bird = N
time = 0
# 새가 없을 때까지 반복
while bird:
    # 최대 시간 값으로 설정
    for i in range(1, N+1):
        # 부를 숫자보다 새가 작으면 처음부터
        if i > bird:
            break
        else:
            time += 1
            bird -= i

print(time)