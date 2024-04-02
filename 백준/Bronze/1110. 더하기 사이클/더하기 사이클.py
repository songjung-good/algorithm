N = int(input())  # 초기 수를 입력 받습니다.
original_N = N  # 초기 수를 저장합니다.
cycle_length = 0  # 사이클의 길이를 저장할 변수를 초기화합니다.

while True:
    tens = N // 10  # 십의 자리 수를 구합니다.
    ones = N % 10  # 일의 자리 수를 구합니다.
    sum_of_digits = tens + ones  # 두 자리 수의 각 자리 수를 더합니다.
    new_number = (ones * 10) + (sum_of_digits % 10)  # 새로운 수를 만듭니다.
    cycle_length += 1  # 사이클의 길이를 증가시킵니다.
    N = new_number  # 다음 수를 현재 수로 업데이트합니다.
    if new_number == original_N:  # 만약 처음 입력한 수로 돌아왔다면 반복문을 종료합니다.
        break

print(cycle_length)  # 사이클의 길이를 출력합니다.
