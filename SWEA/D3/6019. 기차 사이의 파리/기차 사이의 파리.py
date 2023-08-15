T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    # 기차가 닿을 때 까지 파리가 움직일 수 있는 거리
    distance = (D / (A + B)) * F
    
    print(f'#{tc} {distance:.6f}')  # 소수점 아래 6자리까지 출력
