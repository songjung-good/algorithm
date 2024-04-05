T = int(input())  # 테스트 케이스 개수를 입력받음

# 테스트 케이스 개수만큼 반복
for _ in range(T):
    C = int(input())  # 거스름돈을 입력받음

    # 각 동전의 개수를 계산
    quarter = C // 25
    C %= 25
    dime = C // 10
    C %= 10
    nickel = C // 5
    C %= 5
    penny = C

    # 결과 출력
    print(quarter, dime, nickel, penny)
