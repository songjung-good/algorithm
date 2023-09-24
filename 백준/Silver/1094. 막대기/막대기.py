X = int(input())  # 원하는 길이
count = 0

while X > 0:
    # 가장 작은 길이의 막대 (1)부터 시작하여 비트마스킹으로 확인
    if X & 1:
        count += 1
    X >>= 1  # 다음 길이의 막대를 확인하기 위해 오른쪽으로 비트 이동

print(count)
